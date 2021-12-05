import http.client
import json


class Stonk:
    def __init__(self, ticker):
        self.ticker = ticker
        self.currentPrice = None
        self.previousClosePrice = None
        self.pChange = None
        # self.updateStockInfo()

    def updateStockInfo(self):
        try:
            conn = http.client.HTTPSConnection("query1.finance.yahoo.com")
            conn.request("GET", "/v8/finance/chart/" + self.ticker +
                         "?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance")
            jsonData = json.loads(conn.getresponse().read())
            self.currentPrice = jsonData["chart"]["result"][0]["meta"]["regularMarketPrice"]
            self.previousClosePrice = jsonData["chart"]["result"][0]["meta"]["previousClose"]
            self.pChange = (
                (self.currentPrice - self.previousClosePrice) / self.previousClosePrice) * 100
        except Exception as e:
            print('\033[91m' + "ERROR: Failed to get " +
                  self.ticker + " info: " + str(e) + '\033[0m')

    def __str__(self):
        # self.updateStockInfo()
        if self.pChange < 0:
            return (self.ticker + ": $%.2f" % self.currentPrice + " %.2f" % self.pChange + "%")
        elif self.pChange > 0:
            return (self.ticker + ": $%.2f" % self.currentPrice + " %.2f" % self.pChange + "%")
        else:
            return (self.ticker + ": $%.2f" % self.currentPrice + " %.2f" % self.pChange + "%")
