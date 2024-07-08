import pandas as pd

# Read the CSV files into DataFrames
real_estate_df = pd.read_csv('final_dataset.csv')
postal_codes_df = pd.read_csv('postal_codes.csv')

# Assuming 'postal_code' is the common column name in both DataFrames
# Merge the DataFrames on the postal code column
merged_df = pd.merge(real_estate_df, postal_codes_df, on='postal_code', how='left')

# The merged_df now contains the 'Commune' column with the municipality names
# You can inspect the merged DataFrame
print(merged_df.head())

# Optionally, save the merged DataFrame to a new CSV file
merged_df.to_csv('real_estate_with_commune.csv', index=False)


#df.to_excel('final_dataset.xlsx', index=False)