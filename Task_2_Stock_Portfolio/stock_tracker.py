# CodeAlpha Internship
# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("======================================")
print("       STOCK PORTFOLIO TRACKER")
print("======================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "- $", price)

print("\nEnter the stocks you want to buy.")
print("Type 'done' when you have finished.\n")

while True:

    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than zero.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("✅ Stock added successfully!")
        print("Investment:", "$", investment)
        print()

    except ValueError:
        print("❌ Please enter a valid number for quantity.")

# Display portfolio
print("\n======================================")
print("           YOUR PORTFOLIO")
print("======================================")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity

    print(
        stock,
        "| Quantity:", quantity,
        "| Price: $", price,
        "| Value: $", value
    )

print("--------------------------------------")
print("Total Investment Value: $", total_investment)
print("======================================")

# Save portfolio to a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n\n")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        value = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Value: ${value}\n"
        )

    file.write("\n")
    file.write(f"Total Investment Value: ${total_investment}\n")

print("\n✅ Portfolio saved to portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")
