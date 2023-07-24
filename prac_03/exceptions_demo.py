"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when the user enters a non-integer value for either the numerator or the denominator. This is because the int() function is used to convert the user’s input to an integer, and it will raise a ValueError if it cannot perform the conversion.

2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when the user enters 0 for the denominator. This is because division by zero is undefined in mathematics and is not allowed in Python.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter a non-zero denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
