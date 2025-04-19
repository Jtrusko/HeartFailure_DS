import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv(r'C:\Users\trusk\OneDrive\Desktop\heart.csv')  # adjust the path if needed

# Basic overview
print("\n📊 Dataset Preview:")
print(df.head())

print("\n📋 Dataset Info:")
print(df.info())

print("\n📈 Descriptive Statistics:")
print(df.describe())

# Check for missing values
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# Visualize HeartDisease target distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='HeartDisease', data=df)
plt.title("Heart Disease Distribution")
plt.xlabel("Heart Disease (1 = Yes)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Handle categorical variables for correlation
df_encoded = df.copy()
for col in df_encoded.select_dtypes(include='object').columns:
    df_encoded[col] = LabelEncoder().fit_transform(df_encoded[col])

# Correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df_encoded.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
