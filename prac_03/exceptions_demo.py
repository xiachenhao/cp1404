"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? This typically happens if the user enters something that isn't a number
2. When will a ZeroDivisionError occur?  In Python, dividing any number by zero is undefined
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

