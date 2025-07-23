import yfinance as yf

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# --- Settings ---
ticker = 'AAPL'  # You can change this to 'MSFT', 'GOOG', etc.
end_date = datetime.today()
start_date = end_date - timedelta(weeks=8)

# --- Download Data ---
data = yf.download(ticker, start=start_date, end=end_date, interval='1d')

# --- Prepare Data ---
data = data.reset_index()                     # Convert index to column
data['DayName'] = data['Date'].dt.day_name() # Add weekday name
data = data[['Date', 'Close', 'DayName']]     # Only necessary columns

# Filter weekdays only (exclude weekends)
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
data = data[data['DayName'].isin(weekday_order)]

# --- Ensure 'Close' is a 1D Series ---
data['Close'] = data['Close'].astype(float)  # Just in case

# --- Plot ---
plt.figure(figsize=(10, 6))
# Flatten column names if necessary
if isinstance(data.columns, pd.MultiIndex):
	data.columns = ['_'.join([str(i) for i in col if i]) for col in data.columns]

# Use the correct column names for seaborn
sns.boxplot(data=data, x='DayName', y='Close_AAPL', order=weekday_order)
plt.title(f'{ticker} Closing Price by Day of Week (Last 2 Months)')
plt.xlabel('Day of Week')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.tight_layout()
plt.show()
