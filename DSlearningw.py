print("My Data Science Journey")
print("Analyzing Safaricom NSE Data")
import pandas as pd

import pandas as pd

df = pd.read_csv("NSE_SCOM_Safaricom.csv")

print(df.head())

print(df.shape)

print(df.isnull().sum())
stock_data = pd.read_csv("NSE_SCOM_Safaricom.csv")
print(stock_data.head())