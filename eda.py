import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Starting Exploratory Data Analysis (EDA) ---")

# 1. Load Dataset
# Agar aapne file ka naam 'dataset.csv' rakha hai toh yahan wahi naam use karein
try:
    df = pd.read_csv('dataset.csv')
    print(f"Dataset Loaded Successfully! Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
except FileNotFoundError:
    df = pd.read_csv('creditcard.csv')
    print(f"Dataset Loaded Successfully! Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")

# 2. Basic Information
print("\n--- Dataset Columns & Data Types ---")
print(df.info())

print("\n--- Missing Values Check ---")
print(df.isnull().sum().sum(), "missing values found.")

# 3. Class Distribution (Fraud vs Genuine)
print("\n--- Class Distribution ---")
print(df['Class'].value_counts())

# 4. Correlation Matrix
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), cmap='coolwarm', annot=False)
plt.title('Feature Correlation Matrix')
plt.savefig('correlation_matrix.png')
print("\n[SUCCESS] Correlation matrix graph saved as 'correlation_matrix.png'")
print("--- EDA Complete! ---")