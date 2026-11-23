"""A small menu-driven calculator and unit converter."""


# Keep conversion values here so they are easy to update.
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462,
}

MENU_TEXT = """
===== INTERACTIVE CALCULATOR =====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Convert units
6. Quit
"""

CONVERSION_MENU_TEXT = """
===== UNIT CONVERTER =====
1. Kilometres to miles
2. Celsius to Fahrenheit
3. Kilograms to pounds
4. Back to main menu
"""


def read_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, such as 12 or 3.5.")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b, or return a message if b is zero."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b


def kilometres_to_miles(kilometres):
    """Convert kilometres to miles."""
    return kilometres * CONVERSION_FACTORS["km_to_miles"]


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def kilograms_to_pounds(kilograms):
    """Convert kilograms to pounds."""
    return kilograms * CONVERSION_FACTORS["kg_to_pounds"]


def unit_converter():
    """Show the conversion menu until the user returns to the main menu."""
    while True:
        print(CONVERSION_MENU_TEXT)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            kilometres = read_number("Enter kilometres: ")
            print(f"{kilometres} km = {kilometres_to_miles(kilometres):.4f} miles")
        elif choice == "2":
            celsius = read_number("Enter Celsius: ")
            print(
                f"{celsius} C = "
                f"{celsius_to_fahrenheit(celsius):.2f} F"
            )
        elif choice == "3":
            kilograms = read_number("Enter kilograms: ")
            print(f"{kilograms} kg = {kilograms_to_pounds(kilograms):.4f} pounds")
        elif choice == "4":
            return
        else:
            print("Please choose an option from 1 to 4.")


def run_calculation(choice):
    """Read two numbers, run the selected operation and display its result."""
    first_number = read_number("Enter the first number: ")
    second_number = read_number("Enter the second number: ")

    if choice == "1":
        result = add(first_number, second_number)
    elif choice == "2":
        result = subtract(first_number, second_number)
    elif choice == "3":
        result = multiply(first_number, second_number)
    else:
        result = divide(first_number, second_number)

    print("Result:", result)


def main():
    """Run the calculator until the user chooses to quit."""
    while True:
        print(MENU_TEXT)
        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Goodbye!")
            break
        elif choice in ("1", "2", "3", "4"):
            run_calculation(choice)
        elif choice == "5":
            unit_converter()
        else:
            print("Please choose an option from 1 to 6.")


if __name__ == "__main__":
    main()
