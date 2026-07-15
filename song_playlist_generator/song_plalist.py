import random

# Song Playlist Generator

moody_songs = [
    "Hymn for the Weekend - Coldplay (feat. Beyoncé)",
    "Sunflower - Post Malone",
    "Mood - 24kGoldn (feat. Iann Dior)",
    "In the Dark - Swae Lee",
    "Starlight - Sia"
]

dark_haunting_songs = [
    "Daylight - David Kushner",
    "Power - Isak Danielson",
    "Let the World Burn - Chris Grey",
    "Hurt - Nine Inch Nails",
    "The Dark - Anathema"
]

the_weeknd_and_similar = [
    "In the Night - The Weeknd",
    "Save Your Tears - The Weeknd",
    "False Alarm - The Weeknd",
    "The Weekend - SZA",
    "My Love - Majid Jordan"
]

high_energy_rap = [
    "HUMBLE. - Kendrick Lamar",
    "Till I Collapse - Eminem",
    "Rap God - Eminem",
    "Sicko Mode - Travis Scott (feat. Drake)",
    "Alright - Kendrick Lamar"
]

while True:

    print("\n" + "=" * 45)
    print("🎵 Welcome to Niladri's Playlist Generator! 💙")
    print("=" * 45)

    print("\nChoose a playlist category:")
    print("1. Moody Songs 🌙")
    print("2. Dark Haunting Songs 🌑")
    print("3. The Weeknd & Similar 🌃")
    print("4. High Energy Rap 🔥")
    print("5. Exit ❌")

    choice = input("\nEnter your choice (1/2/3/4/5): ")

    if choice == "1":
        songs = moody_songs
        category = "Moody Songs 🌙"

    elif choice == "2":
        songs = dark_haunting_songs
        category = "Dark Haunting Songs 🌑"

    elif choice == "3":
        songs = the_weeknd_and_similar
        category = "The Weeknd & Similar 🌃"

    elif choice == "4":
        songs = high_energy_rap
        category = "High Energy Rap 🔥"

    elif choice == "5":
        print("\n👋 Thanks for using Niladri's Playlist Generator!")
        print("🎧 Keep listening. See you next time!")
        break

    else:
        print("❌ Invalid choice! Try again.")
        continue

    count = int(input(f"\nHow many songs do you want? (1-{len(songs)}): "))

    if 1 <= count <= len(songs):

        playlist = random.sample(songs, count)

        print(f"\n🎧 Your {category} Playlist:\n")

        for i, song in enumerate(playlist, start=1):
            print(f"{i}. {song}")

    else:
        print(f"❌ Please enter a number between 1 and {len(songs)}.")
        continue

    again = input("\n🔄 Generate another playlist? (y/n): ").lower()

    if again != "y":
        print("\n👋 Thanks for using Niladri's Playlist Generator!")
        print("🎶 Have a great day!")
        break
