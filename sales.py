import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'supermarket_sales - Sheet1.csv'  
data = pd.read_csv(file_path)


# # Summary statistics
summary_stats = data.describe(include='all')

# # Check for missing values
missing_values = data.isnull().sum()
data = data.drop(columns=['gross margin percentage'])


# Summary statistics
print(data.describe(include='all'))

# Visualize sales distribution by branch
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Branch')
plt.title('Sales Distribution by Branch')
plt.show()

# Visualize sales distribution by product line
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Product line')
plt.title('Sales Distribution by Product Line')
plt.show()

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Sales trend over time
plt.figure(figsize=(12, 8))
data.groupby('Date')['Total'].sum().plot()
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

# Correlation matrix
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
