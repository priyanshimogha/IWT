# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create a Random Array Dataset
np.random.seed(0)  # For reproducibility
data = np.random.randint(1, 100, size=(100, 3))  # 100 rows, 3 columns

# Convert array to DataFrame (for easier operations and visualizations)
df = pd.DataFrame(data, columns=["Feature1", "Feature2", "Feature3"])

# Displaying the first 5 rows
print("Dataset (First 5 Rows):\n", df.head())

# 2. Perform Some Basic Operations
# Shape of the dataset
print("\nShape of Dataset:", df.shape)

# Basic statistical summary
print("\nBasic Statistics:\n", df.describe())

# Adding a new feature as the sum of Feature1 and Feature2
df['Feature_Sum'] = df['Feature1'] + df['Feature2']
print("\nDataset with New Feature_Sum:\n", df.head())

# Filter: Only rows where Feature1 > 50
filtered_df = df[df['Feature1'] > 50]
print("\nFiltered Data (Feature1 > 50):\n", filtered_df.head())

# 3. Introduce and Handle Missing Values
# Introducing some missing values (NaN) in the 'Feature2' column
df.loc[5:10, 'Feature2'] = np.nan  # Set Feature2 to NaN from index 5 to 10

# Displaying data with missing values
print("\nData with Missing Values (First 15 Rows):\n", df.head(15))

# Check for missing values
print("\nMissing Value Count:\n", df.isnull().sum())

# Option 1: Handle missing values by filling with the mean of the column
df['Feature2_filled'] = df['Feature2'].fillna(df['Feature2'].mean())

# Option 2: Drop rows with missing values
df_dropped = df.dropna()

print("\nData after Filling Missing Values:\n", df.head(15))
print("\nData after Dropping Missing Values:\n", df_dropped.head())

# 4. Visualizations

# 4.1 Boxplot: To detect outliers
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[['Feature1', 'Feature2_filled', 'Feature3']])
plt.title("Boxplot of Features (with Missing Values Handled)")
plt.show()

# 4.2 Scatter Plot: Visualize relationships between Feature1 and Feature2_filled
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Feature1', y='Feature2_filled', data=df)
plt.title("Scatter Plot between Feature1 and Feature2 (Filled)")
plt.xlabel("Feature1")
plt.ylabel("Feature2 (filled)")
plt.show()

# 4.3 Highlighting Missing Values Visually using Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Heatmap to Highlight Missing Values")
plt.show()

# 4.4 Pairplot: Visualizing pairwise relationships
sns.pairplot(df[['Feature1', 'Feature2_filled', 'Feature3']])
plt.show()
