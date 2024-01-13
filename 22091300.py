
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Load the dataset
file_path = 'Military Expenditure.csv'  # Adjust the path if necessary
military_expenditure_df = pd.read_csv(file_path)

# Preparing data for the visualizations

# 1. Trend of Global Military Spending Over Time
global_military_spending = military_expenditure_df.iloc[:, 4:].sum()

# 2. Top 5 Countries by Military Spending in 2018
top_countries_2018 = military_expenditure_df[['Name', '2018']].sort_values(by='2018', ascending=False).head(5)

# 3. Military Spending as a Percentage of GDP for Selected Major Countries
# Selecting major countries for comparison (USA, China, Russia, India, UK)
major_countries = ['United States', 'China', 'Russian Federation', 'India', 'United Kingdom']
major_countries_spending = military_expenditure_df[military_expenditure_df['Name'].isin(major_countries)]

# Transposing the dataset for easier plotting
major_countries_spending_transposed = major_countries_spending.set_index('Name').iloc[:, 3:].T

# 4. Comparison of Military Spending Growth for Selected Countries
# Calculating the growth from 1960 to 2018
growth_comparison = major_countries_spending[['Name', '1960', '2018']]
growth_comparison['Growth'] = (growth_comparison['2018'] - growth_comparison['1960']) / growth_comparison['1960'] * 100

# Creating the dashboard plot
plt.figure(figsize=(18, 12))

# Plot Title
plt.suptitle("Military Expenditure Analysis Dashboard - Saqib Maqbool 22091300", fontsize=16)

# Subplot 1: Trend of Global Military Spending Over Time
plt.subplot(2, 2, 1)
plt.plot(global_military_spending.index, global_military_spending.values, marker='o', color='b')
plt.title("Global Military Spending Over Time")
plt.xlabel("Year")
plt.ylabel("Total Expenditure (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Subplot 2: Top 5 Countries by Military Spending in 2018
plt.subplot(2, 2, 2)
sns.barplot(x='2018', y='Name', data=top_countries_2018, palette='viridis')
plt.title("Top 5 Countries by Military Spending in 2018")
plt.xlabel("Expenditure (USD)")
plt.ylabel("Country")
plt.grid(True)

# Subplot 3: Military Spending as a Percentage of GDP for Selected Major Countries
plt.subplot(2, 2, 3)
sns.lineplot(data=major_countries_spending_transposed, dashes=False)
plt.title("Military Spending of Major Countries Over Time")
plt.xlabel("Year")
plt.ylabel("Expenditure (USD)")
plt.xticks(rotation=45)
plt.grid(True)

# Subplot 4: Comparison of Military Spending Growth
plt.subplot(2, 2, 4)
sns.barplot(x='Name', y='Growth', data=growth_comparison, palette='rocket')
plt.title("Military Spending Growth (1960 - 2018)")
plt.xlabel("Country")
plt.ylabel("Growth Percentage")
plt.grid(True)

# Save the plot
plt.savefig('Military_Expenditure_Dashboard.png')

# Informing that the plot has been saved
print("The plot has been saved as 'Military_Expenditure_Dashboard.png' in the current directory.")
