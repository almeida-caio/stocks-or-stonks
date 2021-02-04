### draft - 1d random walk or stock prices? ###
## https://tradeoptionswithme.com/random-walk-theory/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## working kinda fine for real data 
strArr = ["AAL", "AAPL", "AMZN", "BABA", "BAC", "F", "FB", "GM", "GME", "GOOG", "INTC", "NFLX", "NOK", "PFE", "SNE", "TSLA", "VALE"]
s_label = np.random.randint(0, len(strArr))

market_compData = pd.read_csv("stock-data/" + strArr[s_label] + ".csv", sep = ',')
stock_numpyData = market_compData.to_numpy()

stock_prices = []
for entry in stock_numpyData:
    stock_prices.append(entry[1])

delta = 800
zeroS = np.random.randint(0, len(stock_prices) - delta)

while (stock_prices[zeroS] < 3):
	zeroS = np.random.randint(0, len(stock_prices) - delta)	

finalS = zeroS + delta

x = np.arange(0, delta)
y = stock_prices[zeroS:finalS]

plt.plot(x,y)
plt.show()
