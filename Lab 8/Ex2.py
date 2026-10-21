total = input("Enter the total for your transaction: ")
cash = input("Enter the cash given by the customer: ")
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0
change = float(cash) - float(total)
print("your change is " + str(change))

while change > 0:
    if change >= 1.00:
        dollars += 1
        change -= 1.00
    elif change >= 0.25:
        quarters += 1
        change -= 0.25
    elif change >= 0.10:
        dimes += 1
        change -= 0.10
    elif change >= 0.05:
        nickels += 1
        change -= 0.05
    else:
        pennies += 1
        change -= 0.01

if dollars > 0:
    print("Dollars: " + str(dollars))
if quarters > 0:
    print("Quarters: " + str(quarters))
if dimes > 0:
    print("Dimes: " + str(dimes))
if nickels > 0:
    print("Nickels: " + str(nickels))
if pennies > 0:
    print("Pennies: " + str(pennies))