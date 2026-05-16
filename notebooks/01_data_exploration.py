import os

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create chart output folder if it does not exist
os.makedirs("reports/charts", exist_ok=True)

# Define assets
tickers = ["AAPL", "MSFT"]

# Download historical adjusted close prices
data = yf.download(
    tickers,
    start="2020-01-01",
    end="2024-01-01",
    auto_adjust=False
)["Adj Close"]

# Display first few rows
print("\nFirst 5 rows:")
print(data.head())

# Summary statistics
print("\nSummary statistics:")
print(data.describe())

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Plot historical prices
plt.figure(figsize=(12, 6))

for column in data.columns:
    plt.plot(data.index, data[column], label=column)

plt.title("Historical Asset Prices")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.legend()
plt.grid(True)
plt.savefig("reports/charts/historical_prices.png", bbox_inches="tight")
plt.show()

# Compute daily returns
returns = data.pct_change().dropna()

print("\nDaily returns:")
print(returns.head())

# Plot daily returns
plt.figure(figsize=(12, 6))

for column in returns.columns:
    plt.plot(returns.index, returns[column], alpha=0.7, label=column)

plt.title("Daily Returns")
plt.xlabel("Date")
plt.ylabel("Daily Return")
plt.legend()
plt.grid(True)
plt.savefig("reports/charts/daily_returns.png", bbox_inches="tight")
plt.show()