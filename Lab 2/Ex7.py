# Ask user to enter a temperature in Fahrenheit and convert it to Celsius.
# Name: Hezra Calventas
# Date: 9/4/2026

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * (5 / 9)

print(f"{fahrenheit}°F is equivalent to {celsius}°C.")

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


# Test the function with known temperature conversions.
print(f"32°F is {fahrenheitToCelsius(32)}°C")
print(f"212°F is {fahrenheitToCelsius(212)}°C")
print(f"98.6°F is {fahrenheitToCelsius(98.6)}°C")