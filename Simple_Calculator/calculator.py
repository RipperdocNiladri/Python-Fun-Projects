# ==============================
#      Simple Calculator
# ==============================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b


while True:
    print("\n" + "=" * 40)
    print("          Niladri's Calculator")
    print("=" * 40)
    print("1. Addition        (+)")
    print("2. Subtraction     (−)")
    print("3. Multiplication  (×)")
    print("4. Division        (÷)")
    print("5. Exit")
    print("=" * 40)

    choice = input("Select an operation (1-5): ")

    if choice == "5":
        print("\nThank you for using Niladri's Calculator! 👋")
        break

    if choice not in ("1", "2", "3", "4"):
        print("❌ Invalid choice. Please select 1-5.")
        continue

    try:
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Invalid number. Please enter a valid numeric value.")
        continue

    if choice == "1":
        result = add(num1, num2)
        symbol = "+"

    elif choice == "2":
        result = subtract(num1, num2)
        symbol = "−"

    elif choice == "3":
        result = multiply(num1, num2)
        symbol = "×"

    elif choice == "4":
        result = divide(num1, num2)
        symbol = "÷"

    print("\n" + "-" * 40)
    print(f"Expression : {num1} {symbol} {num2}")
    print(f"Result     : {result}")
    print("-" * 40)
