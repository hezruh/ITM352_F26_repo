num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
def GCD(num1, num2):
    for divisor in range(min(num1, num2) + 1, 1, -1):
        if (num1 % divisor == 0) and (num2 % divisor == 0):
            return divisor
        else:
            continue
print(GCD(num1, num2))