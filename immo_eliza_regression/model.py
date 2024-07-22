import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import RobustScaler
from sklearn.impute import KNNImputer
import joblib
import xgboost as xgb
from scipy.stats import uniform, randint

print("Loading dataset...")
df = pd.read_excel("final_dataset.xlsx")

print("Separating numeric and non-numeric columns...")
numeric_df = df.select_dtypes(include=[np.number])
non_numeric_df = df.select_dtypes(exclude=[np.number])

print("Imputing missing values with KNN Imputer...")
imputer = KNNImputer(n_neighbors=2)
numeric_df_imputed = pd.DataFrame(imputer.fit_transform(numeric_df), columns=numeric_df.columns)

print("Combining imputed numeric and non-numeric data...")
df = pd.concat([numeric_df_imputed, non_numeric_df], axis=1)

print("Encoding categorical data...")
categorical_columns = df.select_dtypes(include=["object"]).columns
for column in categorical_columns:
    df[column] = df[column].astype('category').cat.codes

print("Removing outliers by capping them to the 1st and 99th percentile...")
numeric_columns = numeric_df_imputed.columns
for column in numeric_columns:
    lower_cap = df[column].quantile(0.01)
    upper_cap = df[column].quantile(0.99)
    df[column] = df[column].clip(lower=lower_cap, upper=upper_cap)

print("Applying log transformation to skewed features...")
for column in numeric_columns:
    if df[column].skew() > 0.75:
        df[column] = np.log1p(df[column])

print("Creating new features TotalArea and PricePerSqft...")
df["TotalArea"] = df["LivingArea"] + df["LotArea"]
df["PricePerSqft"] = df["Price"] / df["TotalArea"]

print("Defining features and target variable...")
X = df.drop("Price", axis=1)
y = df["Price"]

print("Splitting data into training and test sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, _, y_train, _ = train_test_split(X_train, y_train, test_size=0.5, random_state=42)

print("Scaling features using RobustScaler...")
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Setting up parameter distributions for RandomizedSearchCV...")
param_dist = {
    'colsample_bytree': uniform(0.7, 0.3),
    'learning_rate': uniform(0.07, 0.13),
    'max_depth': randint(3, 6),
    'subsample': uniform(0.7, 0.3),
    'min_child_weight': randint(1, 4),
    'n_estimators': randint(50, 100)
}

print("Initializing XGBoost model...")
model = xgb.XGBRegressor(random_state=42, objective='reg:squarederror')

print("Starting RandomizedSearchCV for hyperparameter tuning...")
random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=10, cv=2, n_jobs=-1, scoring='neg_mean_absolute_error', random_state=42)
random_search.fit(X_train_scaled, y_train)

print("Best hyperparameters found.")
best_model = random_search.best_estimator_

print("Making predictions and evaluating the model...")
y_pred = best_model.predict(X_test_scaled)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Root Mean Squared Error: {rmse}")
print(f"Mean Absolute Error: {mae}")
print(f"R2 Score: {r2}")

print("Saving the model and scaler...")
joblib.dump(best_model, "xgboost_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Process completed.")
