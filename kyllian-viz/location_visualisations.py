import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset_cleaned = pd.read_csv("cleaned_location_dataset.csv")

dataset_cleaned["PricePerSqM"] = dataset_cleaned["Price"] / dataset_cleaned["TotalArea"]

def remove_outliers(df, column_name):
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]

dataset_cleaned = remove_outliers(dataset_cleaned, "PricePerSqM")

sale_data = dataset_cleaned[dataset_cleaned["TypeOfSale"] == "residential_sale"]
rent_data = dataset_cleaned[dataset_cleaned["TypeOfSale"] == "residential_monthly_rent"]

sns.set(style="whitegrid")

plt.figure(figsize=(15, 10))
province_sale_price = sale_data.groupby("Province")["PricePerSqM"].mean().reset_index()
sns.barplot(x="Province", y="PricePerSqM", data=province_sale_price, palette="coolwarm")
plt.title("Average Price per Square Meter by Province (Residential Sale)")
plt.xlabel("Province")
plt.ylabel("Average Price per Square Meter (€)")
plt.xticks(rotation=45)
plt.grid(True, color="lightgrey")
plt.show()

plt.figure(figsize=(18, 12))
district_sale_price = sale_data.groupby("District")["PricePerSqM"].mean().reset_index()
sns.barplot(x="District", y="PricePerSqM", data=district_sale_price, palette="Spectral")
plt.title("Average Price per Square Meter by District (Residential Sale)")
plt.xlabel("District")
plt.ylabel("Average Price per Square Meter (€)")
plt.xticks(rotation=90)
plt.grid(True, color="lightgrey")
plt.show()

plt.figure(figsize=(18, 12))
region_sale_price = sale_data.groupby("Region")["PricePerSqM"].mean().reset_index()
sns.barplot(x="Region", y="PricePerSqM", data=region_sale_price, palette="Accent")
plt.title("Average Price per Square Meter by Region (Residential Sale)")
plt.xlabel("Region")
plt.ylabel("Average Price per Square Meter (€)")
plt.xticks(rotation=90)
plt.grid(True, color="lightgrey")
plt.show()

plt.figure(figsize=(15, 10))
province_rent_price = rent_data.groupby("Province")["PricePerSqM"].mean().reset_index()
sns.barplot(x="Province", y="PricePerSqM", data=province_rent_price, palette="Pastel1")
plt.title("Average Price per Square Meter by Province (Residential Monthly Rent)")
plt.xlabel("Province")
plt.ylabel("Average Price per Square Meter (€)")
plt.xticks(rotation=45)
plt.grid(True, color="lightgrey")
plt.show()

plt.figure(figsize=(18, 12))
district_rent_price = rent_data.groupby("District")["PricePerSqM"].mean().reset_index()
sns.barplot(x="District", y="PricePerSqM", data=district_rent_price, palette="Dark2")
plt.title("Average Price per Square Meter by District (Residential Monthly Rent)")
plt.xlabel("District")
plt.ylabel("Average Price per Square Meter (€)")
plt.xticks(rotation=90)
plt.grid(True, color="lightgrey")
plt.show()

plt.figure(figsize=(18, 12))
region_rent_price = rent_data.groupby("Region")["PricePerSqM"].mean().reset_index()
sns.barplot(x="Region", y="PricePerSqM", data=region_rent_price, palette="Set3")
plt.title("Average Price per Square Meter by Region (Residential Monthly Rent)")
plt.xlabel("Region")
plt.ylabel("Average Price per Square Meter (€)")
plt.xticks(rotation=90)
plt.grid(True, color="lightgrey")
plt.show()

numeric_cols = dataset_cleaned.select_dtypes(include=[float, int]).columns
correlation_matrix = dataset_cleaned[numeric_cols].corr()

plt.figure(figsize=(15, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="viridis", cbar=True)
plt.title("Correlation Heatmap")
plt.show()

