CurrentPrice = {'Dow_Jones': '28679', 'NASDAQ': '11863', 'AAPL': '121', 'GOOG': '1571', 'TSLA': '446', 'BRKA': '318969', 'BA': '162', 'GE': '6', 'SP_500': '3511', 'S': '8'}

TickerSymbol = input("Please enter the stock ticker symbol that you would like to see the value of: ")

Stock = CurrentPrice.get(TickerSymbol, "not available.")

print("The current value of", TickerSymbol, "is", Stock)