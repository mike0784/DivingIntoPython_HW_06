from portfolio import *

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}


if __name__ == "__main__":
    print("Стоймость портфеля: {0}".format(calculate_portfolio_value(stocks, prices)))
    print("Доходность портфеля: {0}%".format(calculate_portfolio_return(10000.0, 15000.0)))
    prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}    
    print("Самая доходная акция: {0}".format(get_most_profitable_stock(stocks, prices)))