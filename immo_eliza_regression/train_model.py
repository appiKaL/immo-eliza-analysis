import numpy as np
import joblib
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import xgboost as xgb
from scipy.stats import uniform, randint
from data_preprocessing import preprocess_data
import pandas as pd

X_scaled = np.load("X_scaled.npy")
y = np.load("y.npy")

feature_names = X.columns.tolist()
joblib.dump(feature_names, "feature_names.pkl")

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

param_dist = {
    'colsample_bytree': uniform(0.7, 0.3),
    'learning_rate': uniform(0.07, 0.13),
    'max_depth': randint(3, 6),
    'subsample': uniform(0.7, 0.3),
    'min_child_weight': randint(1, 4),
    'n_estimators': randint(50, 100)
}

model = xgb.XGBRegressor(random_state=42, objective='reg:squarederror')

random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=10, cv=2, n_jobs=-1, scoring='neg_mean_absolute_error', random_state=42)
random_search.fit(X_train, y_train)

best_model = random_search.best_estimator_

y_pred = best_model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Root Mean Squared Error: {rmse}")
print(f"Mean Absolute Error: {mae}")
print(f"R2 Score: {r2}")

joblib.dump(best_model, "xgboost_model.pkl")

feature_names = joblib.load("feature_names.pkl")

missing_features = [feature for feature in feature_names if feature not in input_df.columns]
if missing_features:
    print(f"Warning: The following features are missing from the DataFrame: {missing_features}")

available_features = [feature for feature in feature_names if feature in input_df.columns]
input_df = input_df[available_features]