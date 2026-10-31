# 1. Import libraries
import pandas as pd

# 2. Load Safaricom dataset
df = pd.read_csv("NSE_SCOM_Safaricom.csv")

# 3. Display first five records
print(df.head())

# 4. Check dataset dimensions
print("Dataset dimensions:", df.shape)

# 5. Check missing values
print("Missing values:")
print(df.isnull().sum())

# 6. Display column information
print(df.info())