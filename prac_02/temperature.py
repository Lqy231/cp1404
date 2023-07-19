
"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def c_to_f(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {c_to_f(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {f_to_c(fahrenheit):.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()