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
# Calculate descriptive statistics

mean_price = df["Close"].mean()

median_price = df["Close"].median()

standard_deviation = df["Close"].std()

print("Mean:", mean_price)
print("Median:", median_price)
print("Standard Deviation:", standard_deviation)
#stock_price_performance
print("Average closing price:", df["Close"].mean())
print("Highest closing price:", df["Close"].max())
print("Lowest closing price:", df["Close"].min())

#daily returns
#\[R_t=\frac{P_t-P_{t-1}}{P_{t-1}}\times100\]
df["Daily_Return"] = df["Close"].pct_change() * 100

print(df["Daily_Return"].describe())