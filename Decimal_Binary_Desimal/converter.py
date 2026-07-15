# Decimal - Binary - Decimal Converter

def decimal_to_binary(n):
    binary = ""

    if n < 0:
        return "-" + decimal_to_binary(-n)

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary or "0"   # Handles n = 0


def binary_to_decimal(b):
    decimal = 0
    power = 0

    for digit in reversed(b):
        if digit not in ("0", "1"):
            return "Invalid Binary Number"
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal


# === Main Loop ===
while True:
    print("\n=== Binary <-> Decimal Converter ===")
    print("1. Decimal → Binary")
    print("2. Binary → Decimal")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        try:
            dec = int(input("Enter a Decimal Number: "))
            print(f"Binary: {decimal_to_binary(dec)}")
        except ValueError:
            print("Please enter a valid integer.")

    elif choice == "2":
        bin_input = input("Enter a Binary Number: ")
        print(f"Decimal: {binary_to_decimal(bin_input)}")

    elif choice == "3":
        print("Thank you for using the converter! 👋")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")