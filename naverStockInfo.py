#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import BeautifulSoup
import re
import urllib
import urllib2
from html2text import html2text


def naverStockInfo(stockCode):
	url = 'http://finance.naver.com/item/main.nhn?code=' + stockCode
	headers = { 'User-Agent' : 'Python' }
	request = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(request)
	stockText = response.read()
	soup = BeautifulSoup.BeautifulSoup(stockText)

	for x in soup.findAll('div', {'class':'today'}):
		blinds = x.findAll('span', {'class':'blind'})
		icos = x.findAll('span', {'class': re.compile(r"ico")})
		
	#print blinds
	#print icos
	#print html2text(today.decode('ascii', 'ignore'))
	stockTitle = soup.h2.a.string
	stockPrice = html2text(str(blinds[0])).strip()
	stockPriceRateKor = html2text(str(icos[0]).decode('utf-8')).replace("하락", "▼").replace("상승", "▲").strip()
	stockPriceRate = html2text(str(blinds[1])).strip()
	stockPricePercentSymbol = html2text(str(icos[1])).strip()
	stockPricePercent = html2text(str(blinds[2])).strip()
	stockPriceInfo = (stockTitle, stockPrice, stockPriceRateKor, stockPriceRate, stockPricePercentSymbol, stockPricePercent, stockCode)

	Content = "[{6}] {0} : {1}원\n전일대비 {2} {3} {4}{5}%".format(*stockPriceInfo)
	return Content
