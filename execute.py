from naverStockInfo import *

arrStockCode = ['005930', '066570', '005490']

for stockCode in arrStockCode:
	Content = naverStockInfo(stockCode)
	print Content
