import pandas as pd
import matplotlib.pyplot as plt

# Group 11
data = pd.read_csv(r"D:\[2ND YEAR] - THIRD SEMESTER\CPE106L\Ch_11_data_files\breadprice.csv")

# Convert 'Year' column to datetime format
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Sort data by year
data = data.sort_values(by='Year')

# Melt the dataframe to reshape it so that months become rows
melted_data = pd.melt(data, id_vars=['Year'], var_name='Month', value_name='Price')

# Convert 'Price' column to numeric, removing '$' sign
if melted_data['Price'].dtype == 'object':
    melted_data['Price'] = melted_data['Price'].str.replace('$', '').astype(float)

# Create a pivot table to aggregate prices by month
pivot_table = melted_data.pivot_table(index='Year', columns='Month', values='Price')

# Display line plot for each month
plt.figure(figsize=(12, 12))


plt.subplot(3, 1, 1)
plt.subplots_adjust(hspace=0.5)

# Month
for month in pivot_table.columns:
    plt.plot(pivot_table.index, pivot_table[month].round(2), label=month, marker='o')

plt.title('Group 11: (1) Angeles, Hannah (2) Olaso, Syrha (3) Quiambao, Larrline (4) Sarmiento, Jhianne (5) Ursua, Heart\nAverage Price of Bread Over Time (by Month)')
plt.xlabel('Year')
plt.ylabel('Average Price ($)')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.text(0.5, 0.95, 'This graph shows the average price of bread over the years for each month.\nIt reveals any seasonal trends or fluctuations in bread prices throughout the year.',
         horizontalalignment='center', verticalalignment='top', transform=plt.gca().transAxes)

# Year
plt.subplot(3, 1, 2)
data['Average price'] = data.drop('Year', axis=1).mean(axis=1).round(2)  # Calculate the average price for each year
plt.plot(data['Year'], data['Average price'], marker='o', color='orange')
plt.title('Average Price of Bread Over Time (by Year)')
plt.xlabel('Year')
plt.ylabel('Average Price ($)')
plt.grid(True)
plt.xticks(rotation=45)
plt.text(0.5, 0.95, 'This graph shows the average price of bread over the years.\nIt provides an overall trend of bread prices over time.',
         horizontalalignment='center', verticalalignment='top', transform=plt.gca().transAxes)

# Table for year
ax = plt.subplot(3, 1, 3)
ax.axis('off')  # Turn off axis for the table
monthly_avg = pivot_table.mean()
monthly_avg = monthly_avg.round(2)
month_table = ax.table(cellText=[monthly_avg.values], colLabels=monthly_avg.index, loc='center')
month_table.auto_set_font_size(False)
month_table.set_fontsize(10)
month_table.scale(1.2, 1.2)

plt.tight_layout()
plt.show()
