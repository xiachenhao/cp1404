def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


celsius_input = float(input("Enter temperature in Celsius: "))
converted_fahrenheit = celsius_to_fahrenheit(celsius_input)
print(f"The temperature in Fahrenheit is: {converted_fahrenheit:.2f}")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
converted_celsius = fahrenheit_to_celsius(fahrenheit_input)
print(f"The temperature in Celsius is: {converted_celsius:.2f}")
