import yfinance as yf  ## Importing Yahoo Finance Library
from fredapi import Fred     ## Importing Fred library

def yfin_data():
    aapl = yf.download(tickers='AAPL', period='1000d', interval='1d',inplace=True)  # Apple
    google  = yf.download(tickers='GOOG',  period='1000d', interval='1d',inplace=True)  # Google
    amazon  = yf.download(tickers='AMZN',  period='1000d', interval='1d',inplace=True)  # Amazon
    tesla  = yf.download(tickers='TSLA',  period='1000d', interval='1d',inplace=True) #TESLA
    result = pd.merge(aapl, google, on="Date")
    result = result.drop(columns={'Open_x','High_x','Low_x','Open_y','High_y','Low_y','Close_x','Close_y'})
    result = result.rename(columns={'Adj Close_x': 'Apple_Closing','Adj Close_y':'Google_Closing',
                        'Volume_x':'Apple_Volume','Volume_y':'Google_Volume'})
    output = pd.merge(result,amazon, on = "Date")
    output_th = pd.merge(output, tesla , on = "Date")
    output_th = output_th.drop(columns={'Open_x','High_x','Low_x','Open_y','High_y','Low_y','Close_x','Close_y'})
    output_th = output_th.rename(columns={'Adj Close_x': 'Amazon_Closing','Adj Close_y':'Tesla_Closing',
                            'Volume_x':'Amazon_Volume','Volume_y':'Tesla_Volume'})
    final = pd.merge(output_th, df , on = "Date")
    final = final.set_index('Date')
    final_dyn = final.iloc[100:]
    final_dyn = final_dyn.reset_index()
    final_dyn = final_dyn.rename(columns={'index':'Date'})
    
    return aapl google amazon tesla final final_dyn

def fred_data():
    fred = Fred(api_key='0e8891afccdf0b465cf8915bc862e116')
    data = fred.get_series('DFF')
    data = pd.DataFrame(data)
    data  = data.reset_index()
    data  = data.rename(columns={'index':'Date'})
    fred_data = data.iloc[23989:24989]
    return fred_data



