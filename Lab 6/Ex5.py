# Testing the use of assertions

def celsiusToFahrenheit(celsius):
    #convert Celsius to Fahrenheit
    assert celsius >= -273.15, "Temperature cannot be below absolute zero."
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celsiusToFahrenheit(0)) # should print 32.0
print(celsiusToFahrenheit(100)) # should print 212.0
print(celsiusToFahrenheit(-300)) # should raise AssertionError
