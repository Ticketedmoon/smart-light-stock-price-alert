import yfinance as yf
import os
import env
import requests 

class StockChecker:

    period = "0s"
    params = {}
    
    def __init__(self, stock_symbol):
        self.stockTicker = yf.Ticker(stock_symbol)
        self.url = f"https://financialmodelingprep.com/api/v3/profile/{stock_symbol}"
        self.params['apikey'] = env.API_KEY

    def get_stock_price(self):
        response = requests.get(url = self.url, params = self.params)
        return response.json()[0]['price']