# Simple Stock Price

# fonte: https://www.youtube.com/watch?v=JwSS70SZdyM&t=1882s
# fonte: # https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

import yfinance as yf 
import streamlit as st
import pandas as pd 


st.write("""
	# Simple Stock Price App

	Show are the stock closing and volume of Google!

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data on the ticker symbol
tickerData = yf.Ticker(tickerSymbol)

# get the historical price for this ticker symbol
tickerDF = tickerData.history(period='Id', start='2010-5-31', end='2020-5-31')

# open high low close volume dividends stock split
st.write("""
	## Close Price
""")
st.line_chart(tickerDF.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDF.Volume)
