### real stock prices -- plot generator ###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image
from PIL import PngImagePlugin

line_colors = ['#E4C580', '#E862C3']
strArr = ["AAL", "AAPL", "AMZN", "BABA", "BAC", "F", "FB", "GM", "GME", "GOOG", "INTC", "NFLX", "NOK", "PFE", "SNE", "TSLA", "VALE"]

for plot_index in range(0, 1000):
	f = "1-" + str(plot_index) + ".png"
	s_label = np.random.randint(0, len(strArr))

	market_compData = pd.read_csv("stock-data/" + strArr[s_label] + ".csv", sep = ',')
	stock_numpyData = market_compData.to_numpy()

	stock_dates = []
	stock_prices = []
	for entry in stock_numpyData:
		stock_dates.append(entry[0])
		stock_prices.append(entry[1])

	delta = 800
	zeroS = np.random.randint(0, len(stock_prices) - delta)

	while (stock_prices[zeroS] < 3):
		zeroS = np.random.randint(0, len(stock_prices) - delta)	

	finalS = zeroS + delta

	x = np.arange(0, delta)
	y = stock_prices[zeroS:finalS]

	METADATA = {"ticker":str(strArr[s_label]), "start":str(stock_dates[zeroS]), "end":str(stock_dates[finalS-1])}

	plt.plot(x, y, color = line_colors[np.random.randint(0,2)])
	ax = plt.axes()
	ax.set_facecolor('#163170')
	plt.xticks(size = 12, color = 'white')
	plt.yticks(size = 12, color = 'white')

	# plt.grid()
	plt.savefig(f, extension = 'png', facecolor = '#08114A')
	ax.cla()

	# Saving metadata to the image files
	im = Image.open(f)
	meta = PngImagePlugin.PngInfo()

	for entry in METADATA:
	    meta.add_text(entry, METADATA[entry])
	im.save(f, "png", pnginfo=meta)

	# debugging reasons
	# im2 = Image.open(f)
	# print(im2.info)