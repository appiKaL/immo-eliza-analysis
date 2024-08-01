import pandas as pd

excel_file = 'final_dataset.xlsx'

df = pd.read_excel(excel_file)

df.to_csv('final_dataset.csv', index=False)
