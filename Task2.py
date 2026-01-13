prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 320}

portfolio = {}
total = 0

n = int(input("How many stocks do you want to enter: "))

for i in range(n):
    name = input("Enter stock symbol: ").upper()
    qty = int(input("Enter quantity: "))

    if name in prices:
        value = prices[name] * qty
        portfolio[name] = value
        total += value
    else:
        print("Stock not found")

print()
print("Portfolio Value")
print("----------------")

for stock in portfolio:
    print(stock, ":", portfolio[stock])

print("Total Investment:", total)

save = input("Save to file? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("Stock Portfolio\n\n")
    for stock in portfolio:
        file.write(stock + " : " + str(portfolio[stock]) + "\n")
    file.write("\nTotal Investment: " + str(total))
    file.close()
    print("Saved to portfolio.txt")
