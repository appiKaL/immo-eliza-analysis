import pandas as pd

# Load the dataset
df = pd.read_csv('final_dataset.csv')

# Extract unique values for each categorical column
floodingzone_options = df['FloodingZone'].unique().tolist()
kitchen_options = df['Kitchen'].unique().tolist()
peb_options = df['PEB'].unique().tolist()
stateofbuilding_options = df['StateOfBuilding'].unique().tolist()
subtypeofproperty_options = df['SubtypeOfProperty'].unique().tolist()
typeofsale_options = df['TypeOfSale'].unique().tolist()

# Print the unique values
print("FloodingZone options:", floodingzone_options)
print("Kitchen options:", kitchen_options)
print("PEB options:", peb_options)
print("StateOfBuilding options:", stateofbuilding_options)
print("SubtypeOfProperty options:", subtypeofproperty_options)
print("TypeOfSale options:", typeofsale_options)
