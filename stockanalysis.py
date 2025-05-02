stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def priceAt(x):
    """
    Returns the stock price at the given index.
    """
    if x < 0 or x >= len(stock_prices):
        return None
    print(stock_prices[x])

def maxPrice(a, b):
    """
    Returns the maximum stock price between two indices.
    """
    if a < 0 or b >= len(stock_prices) or a > b:
        return None
    print(max(stock_prices[a:b+1]))

def minPrice(a, b):
    """
    Returns the minimum stock price between two indices.
    """
    if a < 0 or b >= len(stock_prices) or a > b:
        return None
    print(min(stock_prices[a:b+1]))

priceAt(10)
maxPrice(0, 5)
minPrice(0, 5)