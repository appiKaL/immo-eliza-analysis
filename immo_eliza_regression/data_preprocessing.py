import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import RobustScaler

def preprocess_data(file_path):
    
    df = pd.read_excel(file_path)

    categorical_columns = df.select_dtypes(include=["object"]).columns
    encoders = {}
    for column in categorical_columns:
        df[column] = df[column].astype('category')
        encoders[column] = df[column].cat.categories
        df[column] = df[column].cat.codes

    numeric_columns = df.select_dtypes(include=["number"]).columns
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

    joblib.dump(encoders, "encoders.pkl")
    joblib.dump(X.columns.tolist(), "feature_names.pkl")

    return X, y

if __name__ == "__main__":
    X, y = preprocess_data("final_dataset.xlsx")
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)
    joblib.dump(scaler, "scaler.pkl")
    np.save("X_scaled.npy", X_scaled)
    np.save("y.npy", y)