# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
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
#stock volatility and risk
volatility = df["Daily_Return"].std()

print("Daily volatility:", volatility)
# 30-day rolling volatility

df["Rolling_Volatility"] = (
    df["Daily_Return"].rolling(window=30).std()
)

print(df["Rolling_Volatility"].tail(10))
#Visualise rolling volatility
#dates
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

df = df.sort_values("Date")

df["Rolling_Volatility"] = (
    df["Daily_Return"].rolling(window=30).std()
)
"""
pd.to_datetime() converts strings into date objects.
%d represents the day.
%m represents the month.
%Y represents the four-digit year.
sort_values() arranges observations chronologically.
rolling(window=30).std() calculates volatility over a moving 30-observation window.
"""
plt.figure(figsize=(12, 6))

plt.plot(
    df["Date"],
    df["Rolling_Volatility"]
)

plt.title("Safaricom 30-Day Rolling Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility (%)")

plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
"""
Peaks: Periods of relatively high volatility.
Troughs: Periods of relatively low volatility.
Sudden increases: Periods when daily returns became more variable.
Long-term patterns: Whether volatility generally increased or decreased.
"""

# MONTHLY STOCK PERFORMANCE ANALYSIS

df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

df["Month_Name"] = df["Date"].dt.month_name()

monthly_prices = df.groupby(
    ["Year", "Month"]
)["Close"].mean()

print("Monthly Average Closing Prices:")
print(monthly_prices)

monthly_close = df.groupby(
    ["Year", "Month"]
)["Close"].last()

monthly_returns = monthly_close.pct_change() * 100

print("Monthly Returns (%):")
print(monthly_returns)

print("Best performing month:")
print(monthly_returns.idxmax(), monthly_returns.max())

print("Worst performing month:")
print(monthly_returns.idxmin(), monthly_returns.min())

import matplotlib.pyplot as plt

monthly_returns.plot(
    figsize=(14, 6),
    title="Safaricom Monthly Stock Returns"
)

plt.xlabel("Year, Month")
plt.ylabel("Monthly Returns (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
# IDENTIFY BEST AND WORST MONTHS

best_month = monthly_returns.idxmax()
worst_month = monthly_returns.idxmin()

print("Best performing month:", best_month)
print("Best monthly return:", round(monthly_returns.max(), 2), "%")

print("Worst performing month:", worst_month)
print("Worst monthly return:", round(monthly_returns.min(), 2), "%")

print("Average monthly return:",
      round(monthly_returns.mean(), 2), "%")

# IMPROVED MONTHLY RETURNS VISUALISATION

plt.figure(figsize=(14, 6))

plt.plot(monthly_returns.index.map(
    lambda x: f"{x[0]}-{x[1]:02d}"
), monthly_returns.values)

plt.axhline(y=0, color="red", linestyle="--")

plt.title("Safaricom Monthly Stock Returns (2012-2019)")
plt.xlabel("Month")
plt.ylabel("Monthly Return (%)")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()