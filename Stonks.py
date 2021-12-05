from Stonk import Stonk
from StonksIterator import StonksIterator


class Stonks:
    def __init__(self, tickers):
        self.stonks = list()
        for ticker in tickers:
            self.stonks.append(Stonk(ticker))

    def __iter__(self):
        return StonksIterator(self.stonks)

    def addStonk(self, ticker):
        self.stonks.append(Stonk(ticker))

