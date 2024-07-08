import pandas as pd

real_estate_df = pd.read_csv('final_dataset.csv')
postal_codes_df = pd.read_csv('new_postal_code.csv')

merged_df = real_estate_df.merge(postal_codes_df, how='left', on='PostalCode')
merged_df.to_csv('dataset_municipalities.csv', index=False)