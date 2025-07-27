stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 120
}

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker!")

while True:
    stock = input("Enter stock symbol (AAPL, TSLA, GOOG, MSFT, AMZN or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    investment = stock_prices[stock] * quantity
    portfolio[stock] = investment
    total_investment += investment

print("\nPortfolio Summary:")
for stock, investment in portfolio.items():
    print(f"{stock}: ${investment}")

print(f"Total Investment: ${total_investment}")

save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        for stock, investment in portfolio.items():
            file.write(f"{stock}: ${investment}\n")
        file.write(f"Total Investment: ${total_investment}\n")
    print("Saved to portfolio.txt")
