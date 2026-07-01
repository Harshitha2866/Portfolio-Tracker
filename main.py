# -------------------------------
# Portfolio Tracker
# -------------------------------

def calculate_values(quantity, buying_price, current_price):
    investment = quantity * buying_price
    current_value = quantity * current_price
    profit_loss = current_value - investment
    return investment, current_value, profit_loss


portfolio = []

print("===================================")
print("     STOCK PORTFOLIO TRACKER")
print("===================================")

num = int(input("Enter the number of stocks: "))

for i in range(num):
    print("\nEnter details for Stock", i + 1)

    stock_name = input("Stock Name: ")
    quantity = int(input("Quantity: "))
    buying_price = float(input("Buying Price: "))
    current_price = float(input("Current Price: "))

    investment, current_value, profit_loss = calculate_values(
        quantity,
        buying_price,
        current_price
    )

    stock = {
        "name": stock_name,
        "quantity": quantity,
        "buy_price": buying_price,
        "current_price": current_price,
        "investment": investment,
        "current_value": current_value,
        "profit_loss": profit_loss
    }

    portfolio.append(stock)

print("\n===================================")
print("        PORTFOLIO REPORT")
print("===================================")

total_investment = 0
total_current_value = 0
total_profit_loss = 0

for stock in portfolio:

    print("\nStock Name :", stock["name"])
    print("Quantity   :", stock["quantity"])
    print("Buy Price  :", stock["buy_price"])
    print("Current Price :", stock["current_price"])
    print("Investment :", stock["investment"])
    print("Current Value :", stock["current_value"])

    if stock["profit_loss"] > 0:
        print("Status : PROFIT")
        print("Profit :", stock["profit_loss"])
    elif stock["profit_loss"] < 0:
        print("Status : LOSS")
        print("Loss :", abs(stock["profit_loss"]))
    else:
        print("Status : NO PROFIT NO LOSS")

    total_investment += stock["investment"]
    total_current_value += stock["current_value"]
    total_profit_loss += stock["profit_loss"]

print("\n===================================")
print("      OVERALL SUMMARY")
print("===================================")

print("Total Investment :", total_investment)
print("Current Portfolio Value :", total_current_value)

if total_profit_loss > 0:
    print("Overall Profit :", total_profit_loss)
elif total_profit_loss < 0:
    print("Overall Loss :", abs(total_profit_loss))
else:
    print("No Profit No Loss")

print("\nThank you for using Portfolio Tracker!")