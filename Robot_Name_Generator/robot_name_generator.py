import random

# Define robot parts
prefixes = ["XR", "ZK", "BOT", "ALPHA", "MEGA", "CY"]
middles = ["-A", "-Z", "-N", "-X", "-B", "-R"]
suffixes = ["100", "2000", "X5", "99", "MK3", "3001"]

# === Main Loop ===
while True:
    try:
        count = int(input("\nHow many robots do you want to generate? "))

        if count <= 0:
            print("Please enter a positive number.")
            continue

        # Maximum unique combinations
        max_combinations = len(prefixes) * len(middles) * len(suffixes)

        if count > max_combinations:
            print(f"Maximum unique robots possible: {max_combinations}")
            continue

        print(f"\nGenerating {count} robot(s)...\n")

        robot_names = set()

        while len(robot_names) < count:
            name = (
                random.choice(prefixes)
                + random.choice(middles)
                + random.choice(suffixes)
            )
            robot_names.add(name)

        for i, name in enumerate(robot_names, start=1):
            print(f"🤖 Robot {i}: {name}")

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Ask if the user wants another round
    again = input("\nGenerate more robots? (y/n): ").strip().lower()

    if again != "y":
        print("\n👋 Thanks for using the Robot Name Generator!")
        break
