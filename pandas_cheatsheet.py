import numpy as np
import pandas as pd
from datetime import time

#See following links for refernce:
#https://pandas.pydata.org/ for reference
#http://nbviewer.jupyter.org/gist/wesm/4757075/PandasTour.ipynb

def custom_resampler(array_like):
	return np.mean(array_like), np.median(array_like), np.std(array_like)


def pandas_basics_demo():
	temp = "data/%s.csv"
	path = temp % 'AAPL'

	#Read csv file and load it as pandas data frame
	aapl = pd.read_csv(temp % 'AAPL')
	print "AAPL stock data loaded/parsed as a DataFrame:\n", aapl.head(5), "\n-----------------------"
	print "AAPL stock data frame - reading Date column --> aapl.Date:", aapl.Date.head(5), "\n-----------------------"
	
	#Use Date for dataframe index
	aapl.index = pd.to_datetime(aapl.pop('Date'))

	#Show close price on 2008-10-14
	print "AAPL Close price on 2008-10-14", aapl.Close['2008-10-14'], "\n-----------------------"

	#resample months - resample behaves like group by and then apply mean, median and std stats to time series
	mth_mean = aapl.Close.resample('M', how=['mean', 'median', 'std'])
	print "mth mean:", mth_mean.head(5), "\n-----------------------"

	close = aapl.Close
	#Shift index by 1 day for computing relative close price change over time
	print "Close price relative percentage change based on the previous day:", (close / close.shift(1) - 1).head(5), "\n-----------------------"


def pandas_data_alignment():
	#Create a time series, firts parameter is the data and second one is index
	ts1 = pd.Series(np.random.randn(10), index=pd.date_range('1/1/2000', periods=10))
	print "ts1:\n", ts1, "\n-----------------------"
	
	ts2 = ts1[[0, 2, 4, 5, 6, 7, 8]]
	print "ts2 is a subsample of ts1:\n", ts2, "\n-----------------------"

	print "sum of ts1+ts2:\n", ts1 + ts2, "\n-----------------------"

	#Let's create a data frame from ts1 and ts2
	df = pd.DataFrame({'A': ts1, 'B': ts2})
	print "Data frame created from ts1 & ts2 (ts2 have some missing values!):\n", df, "\n-----------------------"

	#Missing data handling
	print "df count per column (pandas ignores NaN):\n", df.count(), "\n-----------------------"
	print "df sum per column (pandas ignores NaN):\n", df.sum(), "\n-----------------------"
	print "df mean  per column (pandas ignores NaN):\n", df.mean(), "\n-----------------------"

	print "Use dropna() removes if there is any missing value:\n", df.dropna(), "\n-----------------------"

	print "Use fillna(0) method to replace NaN with 0:\n", df.fillna(0), "\n-----------------------"

	print "Use fillna(method='ffill') to propagate last valid observation forward:\n", df.fillna(method='ffill'), "\n-----------------------"

	# df.asfreq('4h')

if __name__ == "__main__":
	#pandas_basics_demo()
	pandas_data_alignment()
