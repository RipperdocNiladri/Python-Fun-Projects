import random

coins = 0
high_score = 0
win_streak = 0

print("=" * 50)
print("🎮 Welcome to Niladri's Number Guessing Game 🎮")
print("=" * 50)

while True:

    print("\nChoose Difficulty")
    print("1. Easy   (1-20)   ❤️ 7 Lives")
    print("2. Medium (1-50)   ❤️ 6 Lives")
    print("3. Hard   (1-100)  ❤️ 5 Lives")

    while True:
        difficulty = input("\nEnter choice (1/2/3): ")

        if difficulty == "1":
            max_number = 20
            lives = 7
            reward = 20
            break

        elif difficulty == "2":
            max_number = 50
            lives = 6
            reward = 40
            break

        elif difficulty == "3":
            max_number = 100
            lives = 5
            reward = 70
            break

        else:
            print("❌ Invalid choice!")

    secret = random.randint(1, max_number)
    attempts = 0

    print(f"\nGuess the number between 1 and {max_number}")

    while lives > 0:

        try:
            guess = int(input(f"\n❤️ Lives: {lives} | Enter Guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        attempts += 1

        if guess == secret:

            coins += reward
            win_streak += 1

            if high_score == 0 or attempts < high_score:
                high_score = attempts

            messages = [
                "🎉 Incredible!",
                "🔥 You nailed it!",
                "😎 Genius!",
                "🚀 Amazing Guess!",
                "🏆 Champion!"
            ]

            print("\n" + random.choice(messages))
            print(f"✅ Correct Number: {secret}")
            print(f"🎯 Attempts : {attempts}")
            print(f"💰 Coins Earned : +{reward}")
            print(f"💵 Total Coins : {coins}")
            print(f"🔥 Win Streak : {win_streak}")

            break

        elif guess < secret:
            print("📈 Higher!")

        else:
            print("📉 Lower!")

        lives -= 1

    if lives == 0:
        print("\n💀 Game Over!")
        print(f"The number was {secret}")
        win_streak = 0

    print("\n" + "-" * 40)
    print(f"💰 Coins      : {coins}")
    print(f"🏆 High Score : {high_score if high_score else 'None'} attempts")
    print(f"🔥 Streak     : {win_streak}")
    print("-" * 40)

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        print("\nThanks for playing! 👋")
        break
