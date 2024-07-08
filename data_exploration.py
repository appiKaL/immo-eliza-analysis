import json
import pandas as pd

with open('denis-immoscraper/data/output.json') as file:
    json_data = json.load(file)
    
df = pd.json_normalize(json_data)
df.to_csv('output.csv', index=False)

df_csv = pd.read_csv('output.csv')
df_csv.to_excel('output.xlsx', index=False)