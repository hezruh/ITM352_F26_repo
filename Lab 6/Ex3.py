# determine the movie price. rules are:
"""
normal price = $14
65+, $8
tues, $10
matinee, price = $5 for seniors, $8 otherwise
Name: Hezra Calventas
Date: Sep 25, 2026
"""

age = 82
day = "Tuesday"
matinee = True

price = 14

if day == "Tuesday":
    price = 10

if age >= 65:
    price = 8

if matinee:
    if age >= 65:
        price = 5
    else:
        price = 8

print("Ticket price is $", price)

print(f"Day: {day}, Matinee: {matinee}")
if age >= 65:
    print("welcome boomer")
else:
    print("welcome zoomer")

print(f"Ticket price is ${price:.2f}")
