import pandas as pd

df = pd.read_csv("final_dataset.csv")
df = df[["Url","Price", "Country", "District", "Locality", "PostalCode", "PropertyId", "Province", "Region", "TypeOfSale", "LivingArea", "GardenArea"]]
df = df[((df["PostalCode"] >= 1000) & (df["PostalCode"] <= 9999 ))]
df["GardenArea"] = df["GardenArea"].fillna(0)
df["TotalArea"] = df["LivingArea"] + df["GardenArea"]
df_dropped = df.dropna()
df_dropped.to_csv("cleaned_location_dataset.csv", index=False)