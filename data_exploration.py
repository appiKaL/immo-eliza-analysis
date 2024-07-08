import json
import pandas as pd

with open('denis-immoscraper/data/final_dataset.json') as file:
    json_data = json.load(file)
    
keys = json_data.keys()

inner_keys = next(iter(json_data.values())).keys()

data_list = []

for inner_key in inner_keys:
    entry = {}
    for key in keys:
        entry[key] = json_data[key].get(inner_key)
    data_list.append(entry)
    
df = pd.DataFrame(data_list)
df.to_csv('final_dataset.csv', index=False)
df.to_excel('final_dataset.xlsx', index=False)