import pandas as pd
import matplotlib.pyplot as plt

# Reading dataset
dataset_cleaned = pd.read_csv("clean_dataset.csv")

# PEB simplify
dataset_cleaned['PEB_Simplified'] = dataset_cleaned['PEB'].str.extract(r'(A\+\+|A\+|A|B|C|D|E|F|G)', expand=False).fillna('Unknown')

# Calculate the counts of each PEB_Simplified class within each District
class_counts = dataset_cleaned.groupby(['Region', 'PEB_Simplified']).size().reset_index(name='ClassCount')

# Calculate total counts for each District
total_counts = dataset_cleaned.groupby('Region').size().reset_index(name='TotalCount')

# Merge class counts with total counts
merged_data = class_counts.merge(total_counts, on='Region')

# Calculate the proportion of each PEB_Simplified class within each District
merged_data['Proportion'] = merged_data['ClassCount'] / merged_data['TotalCount'] * 100

# Create pie charts for each district
districts = merged_data['Region'].unique()

# Plotting
fig, axes = plt.subplots(len(districts)//4 + 1, 4, figsize=(20, 20))
axes = axes.flatten()

for i, district in enumerate(districts):
    ax = axes[i]
    district_data = merged_data[merged_data['Region'] == district]
    ax.pie(district_data['Proportion'], labels=district_data['PEB_Simplified'], autopct='%1.1f%%', startangle=140)
    ax.set_title(district)

# Remove empty subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
