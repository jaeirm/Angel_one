import yfinance as yf
import pandas as pd

# Fetch stock data for Apple (AAPL)
tic = "TCS.NS"
stock = yf.Ticker(tic)

# Get stock info
stock_info = stock.info
print(stock_info)

# Get historical market data
hist = stock.history(period="1mo")
print(hist)

# Save to CSV
file = f"{tic}.csv"
hist.to_csv(file)
