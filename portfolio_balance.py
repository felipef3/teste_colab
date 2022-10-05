import pandas as pd

class PortifolioBalance:
    
    def __init__(self,tickers):
        self.tickers = tickers
        self.calcular_balanco()
        
    def calcular_balanco(self):
        
        yield_total = 0
        for y in self.tickers:
            yield_total = yield_total + y['yield']# ** 2
            
        for y in self.tickers:
            y['yield_relativo'] = (y['yield']) / yield_total
            
    def show(self):
        df = pd.DataFrame(self.tickers)
        return df
    
    def calcular_aporte(self,valor_aporte):
        df = self.show()
        df['aporte'] = df['yield_relativo'] * valor_aporte
        return df