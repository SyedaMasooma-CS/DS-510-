Final Project
#Dependencies

 numpy==1.21.5
 pandas==1.4.4
 matplotlib==3.5.2
 yfinance==0.1.87
 fredapi==0.5.0
 sklearn==1.0.2
 scipy==1.9.1
 seaborn==0.11.2
 cufflinks==0.17.3
 statsmodels==0.13.2

#Installation

...
pip install -r requirements.txt
...


# Running the project

...
Python Jupyter Notebook
Final Code.ipynb
Use:
Cell->Run All

# The notebook contains
Data Collection
Data Preprocessing
Data Visualization
Exploratory Data Analysis
...
#Data Collection and Preprocessing
- Used fred api key to get Federal Board of Revenue Interest Rate Data
- Used yfinance library to get stock market data 
- Merge the files on the unique variable 'Date'
- Get all the variables of interest in one dataframe for analysis

# Methodoloy
- Exploratory Data Analysis
- Statistical Modelling for Inferences on the Data
-
# Visualization
- Since the data is timeseries and I need to look at the trends in data over time and relationship between trends of different variables, I have made mutilple plots.
- These include line plots and scatter plot of individual variables over Date.
- I have made lineplots of different variables in the same plot to visualize the comparison between trends.
- I have made interactive plots to see more detail of the data including growth and decline. I have tried to use more engaging colors to make the visualization more interpretable

#Data Analysis

- Pearson Correlation b/w Interest Rate and Stock Market prices
- Logistic Regression to predict increase in stock market at quarter end
- Dickey Fuller Test to check Stationarity of Stock Market Prices and Interest R  ate
- Checking Autocorrelation of these series
- Fitting ARMA on Apple Stock Prices Growth Rate
- Fitting ARMA on Interest Rate Growth

#Future Work

- More Advanced Forecasting Techniques
- Include more historic data
- Analyze trends at time of historic economic importance

