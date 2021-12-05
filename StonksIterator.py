class StonksIterator:
    def __init__(self, stonks):
        self.stonks = stonks
        self.index = 0

    def __next__(self):
        if self.index < (len(self.stonks)):
            result = (self.stonks[self.index])
            self.index += 1
            return result
        raise StopIteration
