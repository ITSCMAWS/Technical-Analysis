import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

# Fetching data for Microsoft (MSFT) for the past 10 years
msft_data = yf.download('MSFT', start='2013-01-01', end='2023-01-01')

msft_data['MA50'] = msft_data['Close'].rolling(window=50).mean()
msft_data['MA200'] = msft_data['Close'].rolling(window=200).mean()

# Creating a figure and a plot
apds = [mpf.make_addplot(msft_data['MA50'], color='blue', width=0.7), 
        mpf.make_addplot(msft_data['MA200'], color='red', width=0.7)]

# Candlestick plot with moving averages
mpf.plot(msft_data, type='candle', style='yahoo', addplot=apds, 
         title="Microsoft Stock - 50 & 200 Day Moving Averages", 
         ylabel="Price ($)", volume=True)

crossover_up = (msft_data['MA50'] > msft_data['MA200']) & (msft_data['MA50'].shift(1) <= msft_data['MA200'].shift(1))
crossover_down = (msft_data['MA50'] < msft_data['MA200']) & (msft_data['MA50'].shift(1) >= msft_data['MA200'].shift(1))

for date in msft_data[crossover_up].index:
    plt.annotate('↑', (date, msft_data.loc[date, 'MA50']), textcoords="offset points", xytext=(0,10), ha='center', color='green')

for date in msft_data[crossover_down].index:
    plt.annotate('↓', (date, msft_data.loc[date, 'MA200']), textcoords="offset points", xytext=(0,-15), ha='center', color='red')
