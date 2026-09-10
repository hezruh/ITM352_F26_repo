'''
Create a function—call it midpoint —that takes two numbers as input and returns the value halfway between them. 
'''
num1 = int(input("Enter the lower number: "))
num2 = int(input("Enter the higher number: "))

def midpoint(num1, num2):
    return int((num1 + num2) / 2)

print(f"The midpoint between {num1} and {num2} is: {midpoint(num1, num2)}")
