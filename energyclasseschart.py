import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading dataset
dataset_cleaned = pd.read_csv("clean_dataset.csv")

# PEB simplify
dataset_cleaned['PEB_Simplified'] = dataset_cleaned['PEB'].str.extract(r'(A\+\+|A\+|A|B|C|D|E|F|G)', expand=False).fillna('Unknown')

# Calculate the counts of each PEB_Simplified class within each District
class_counts = dataset_cleaned.groupby(['District', 'PEB_Simplified']).size().reset_index(name='ClassCount')

# Calculate total counts for each District
total_counts = dataset_cleaned.groupby('District').size().reset_index(name='TotalCount')

# Merge class counts with total counts
merged_data = class_counts.merge(total_counts, on='District')

# Calculate the proportion of each PEB_Simplified class within each District
merged_data['Proportion'] = merged_data['ClassCount'] / merged_data['TotalCount'] * 100

# Plotting the proportions
plt.figure(figsize=(14, 8))
sns.barplot(data=merged_data, x='District', y='Proportion', hue='PEB_Simplified')
plt.xticks(rotation=90)
plt.title('Proportion of Energy Classes by Region')
plt.xlabel('District')
plt.ylabel('Proportion (%)')
plt.legend(title='Energy Class')
plt.tight_layout()
plt.show()
