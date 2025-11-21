# Stock prices
stock_prices = {"AIRTEL": 180, "TCS": 250, "HDFC": 300, "RELIANCE": 2800, "CODE ALPHA": 3000}

portfolio = {}
total_value = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in dictionary!")
        continue
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate total
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares → ₹{value}")

print("\nTotal Investment Value: ₹", total_value)

# Optional: Save to file
with open("portfolio.txt", "w", encoding="utf-8") as f:
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares → ₹{stock_prices[stock] * qty}\n")
    f.write(f"\nTotal Investment Value: ₹{total_value}")