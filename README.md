Project Description

-	Our goal is to test the performance off 3 major trading indicators that generate buy and sell signals to test their performance over a given time series on 3 major stock assets

- All indicators are oscillators, meaning they oscillate between a range of values

Indicators:
-	MACD – Moving Average Convergence Divergence
-	RSI – Relative Strength Indicator
-	Stochastic Indicator

Assets:
- TSLA – Tesla
-	GOOG – Google
-	AAPL – Apple

-	Weekly time series be used on the above-mentioned assets. Final analysis conducted on the price close of each asset over the time series.

Data Source:
-	Stock data and indicator data relative to the above assets has been taken from www.alphavantage.co. Utilising the API, JSON data has been extracted then converted in data frames for analysis

Final Output:
-	Combined time series with buy/sell signals for each indicator along with the amount of shares and capital remaining after each time interval
