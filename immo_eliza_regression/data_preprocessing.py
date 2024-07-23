import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
from sklearn.impute import SimpleImputer
import joblib

def preprocess_data(filepath):
    df = pd.read_excel(filepath)

    numeric_df = df.select_dtypes(include=[np.number])
    non_numeric_df = df.select_dtypes(exclude=[np.number])

    imputer = SimpleImputer(strategy='mean')
    numeric_df_imputed = pd.DataFrame(imputer.fit_transform(numeric_df), columns=numeric_df.columns)

    df = pd.concat([numeric_df_imputed, non_numeric_df], axis=1)

    categorical_columns = df.select_dtypes(include=["object"]).columns
    for column in categorical_columns:
        df[column] = df[column].astype('category').cat.codes

    numeric_columns = numeric_df_imputed.columns
    for column in numeric_columns:
        lower_cap = df[column].quantile(0.01)
        upper_cap = df[column].quantile(0.99)
        df[column] = df[column].clip(lower=lower_cap, upper=upper_cap)

    for column in numeric_columns:
        if df[column].skew() > 0.75 and column != 'Price':
            df[column] = np.log1p(df[column])

    df["TotalArea"] = df["LivingArea"] + df["GardenArea"]
    df["RoomToAreaRatio"] = df["RoomCount"] / df["TotalArea"]
    df["BedroomToAreaRatio"] = df["BedroomCount"] / df["TotalArea"]
    df["BathroomToBedroomRatio"] = df["BathroomCount"] / df["BedroomCount"]
    df["LivingAreaToTotalArea"] = df["LivingArea"] / df["TotalArea"]
    df["GardenAreaToTotalArea"] = df["GardenArea"] / df["TotalArea"]
    df["LivingAreaToRoomCount"] = df["LivingArea"] / df["RoomCount"]
    df["AgeOfBuilding"] = 2024 - df["ConstructionYear"]

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)

    X = df.drop("Price", axis=1)
    y = df["Price"]

    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, "scaler.pkl")

    print(f"Number of data points: {X.shape[0]}")
    print(f"Number of features: {X.shape[1]}")

    return X_scaled, y

if __name__ == "__main__":
    X_scaled, y = preprocess_data("final_dataset.xlsx")
    np.save("X_scaled.npy", X_scaled)
    np.save("y.npy", y)
