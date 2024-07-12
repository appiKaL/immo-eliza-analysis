# Immo Eliza Analysis Project

## Overview

The Immo Eliza Analysis Project aims to analyze property data in Belgium to understand various factors influencing property prices. The analysis includes data cleaning, visualization, and preparation for training a predictive model to estimate house and apartment prices. This project is structured in a Jupyter notebook, which narrates the analysis process with markdown explanations and corresponding code cells.

![Real Estate Analysis](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2l2dDJwMnBneG9pN3I1ZTdnYzJweXN1OGxycjZmYzdrN3FucDZ4NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5wWf7GMbT1ZUGTDdTqM/giphy.webp)

## Dataset

The dataset includes details about properties such as price, location, type of sale, and various physical characteristics. It consists of the following columns:

- Url
- Price
- Country
- District
- Locality
- PostalCode
- PropertyId
- Province
- Region
- TypeOfSale
- LivingArea
- GardenArea
- TotalArea

## Analysis Process

The analysis process is divided into the following steps:

### 1. Data Loading

We begin by loading the dataset and inspecting its structure to understand the available columns and the type of data we are dealing with.

### 2. Data Cleaning

To ensure the accuracy of our analysis, we clean the dataset by calculating the price per square meter and removing outliers that might skew our results.

### 3. Data Visualization

We create bar plots to visualize the average price per square meter for residential sales and monthly rents by province, district, and region. Each plot is generated in separate cells for better readability and interpretation.

### 4. Correlation Analysis

Finally, we create a correlation heatmap to explore the relationships between different numeric variables in the dataset. This helps us understand how different factors are related to property prices.

## Jupyter Notebook

The analysis is presented in a Jupyter notebook with markdown explanations and code cells. The notebook is divided into sections, each performing a specific part of the analysis.

### Notebook Structure

1. **Introduction**
   - Explanation of the project and its goals.

2. **Data Loading**
   - Loading the dataset and initial inspection.

3. **Data Cleaning**
   - Handling missing values, outliers, and calculations.

4. **Data Visualization**
   - Generating bar plots for residential sales and monthly rents by province, district, and region.

5. **Correlation Analysis**
   - Generating a correlation heatmap with as many numeric columns as possible.

## How to Run the Notebook

1. Clone the repository to your local machine.
2. Ensure you have Jupyter Notebook installed. If not, install it using `pip install notebook`.
3. Navigate to the project directory and open the Jupyter Notebook using the command `jupyter notebook`.
4. Open the `Immo_Eliza_Analysis.ipynb` notebook and run the cells in sequence to see the analysis process and results.

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
- Jupyter Notebook

## Conclusion

This project provides insights into the property prices in Belgium through data analysis and visualization. The cleaned and visualized data is prepared for training a predictive model to estimate property prices, which can be a valuable tool for real estate analysis and decision-making.
