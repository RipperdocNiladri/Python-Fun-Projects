# ==================================
#    Secure Password Generator
# ==================================

import secrets
import string

print("=" * 45)
print("     🔐 Password Generator")
print("=" * 45)

while True:

    # Password Length
    while True:
        try:
            length = int(input("\nEnter password length (minimum 4): "))

            if length >= 4:
                break
            else:
                print("❌ Password must be at least 4 characters long.")

        except ValueError:
            print("⚠️ Please enter a valid number.")

    # Character Options
    upper = input("Include Uppercase Letters? (y/n): ").lower()
    lower = input("Include Lowercase Letters? (y/n): ").lower()
    numbers = input("Include Numbers? (y/n): ").lower()
    symbols = input("Include Symbols? (y/n): ").lower()

    characters = ""

    if upper == "y":
        characters += string.ascii_uppercase

    if lower == "y":
        characters += string.ascii_lowercase

    if numbers == "y":
        characters += string.digits

    if symbols == "y":
        characters += string.punctuation

    if characters == "":
        print("\n❌ You must select at least one character type!")
        continue

    # Number of Passwords
    while True:
        try:
            amount = int(input("\nHow many passwords do you want to generate? "))

            if amount > 0:
                break
            else:
                print("❌ Enter a positive number.")

        except ValueError:
            print("⚠️ Please enter a valid number.")

    print("\n" + "=" * 45)
    print("Generated Passwords")
    print("=" * 45)

    for i in range(1, amount + 1):
        password = ""

        for _ in range(length):
            password += secrets.choice(characters)

        print(f"{i}. {password}")

    print("=" * 45)

    again = input("\nGenerate Again? (y/n): ").lower()

    if again != "y":
        print("\n👋 Thank you for using My Password Generator!")
        break