import yfinance as yf  ## Importing Yahoo Finance Library
from fredapi import Fred     ## Importing Fred library

def yfin_data():
    aapl = yf.download(tickers='AAPL', period='1000d', interval='1d',inplace=True)  # Apple
    google  = yf.download(tickers='GOOG',  period='1000d', interval='1d',inplace=True)  # Google
    amazon  = yf.download(tickers='AMZN',  period='1000d', interval='1d',inplace=True)  # Amazon
    tesla  = yf.download(tickers='TSLA',  period='1000d', interval='1d',inplace=True) #TESLA

def fred_data:
    fred = Fred(api_key='0e8891afccdf0b465cf8915bc862e116')
    data = fred.get_series('DFF')
