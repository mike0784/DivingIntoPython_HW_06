import pickle
import operator
__all__ = ["calculate_portfolio_value", "calculate_portfolio_return", "get_most_profitable_stock"]

__ll__ = {}

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    savePrices(prices)
    ls = list(stocks.keys())
    total = 0.0
    for item in ls:
        total += stocks[item] * prices[item]
    return total

def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    result = (current_value * 100) / initial_value - 100
    return result

def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    lst = readPicess()
    ls = list(stocks.keys())
    maxValue = 0
    maxItem = ""
    result = {}
    for item in ls:
        pp = stocks[item] * (prices[item] - lst[item])
        if pp > maxValue:
            maxValue = pp
            maxItem = item
    return maxItem

def savePrices(prices: dict):
    f = open('myfile.bin', 'wb')
    pickle.dump(prices, f)
    f.close()

def readPicess() -> dict:
    f = open('myfile.bin', 'rb')
    result = pickle.load(f)
    f.close()
    return result
