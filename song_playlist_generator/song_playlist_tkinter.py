import tkinter as tk
from tkinter import ttk, messagebox
import random


# Your playlists
playlists = {
    "Haunting Vibes": ["After Hours", "Call Out My Name", "Creepin", "Wicked Games", "In the Night", "Sign of the Times"],
    "Rap Hype": ["Godzilla", "Rap God", "Not Afraid", "Lose Yourself", "Mockingbird", "Runaway"],
    "Moody Feels": ["Blinding Lights", "Starboy", "Save Your Tears", "Die for You", "The Hills", "Cold Heart"]
}


# Create main window
root = tk.Tk()
root.title("Niladri's Playlist Genarator 💚")
root.geometry("400x400")


# Playlist type
tk.Label(root, text="🎶 Choose Playlist Type:").pack(pady=5)
playlist_var = tk.StringVar()
playlist_dropdown = ttk.Combobox(
    root, textvariable=playlist_var, values=list(playlists.keys()))
playlist_dropdown.pack()


# Number of songs
tk.Label(root, text="🔢 Number of Songs:").pack(pady=5)
num_var = tk.StringVar()
tk.Entry(root, textvariable=num_var).pack()


# Result Box
result_box = tk.Text(root, height=10, width=40)
result_box.pack(pady=10)


# Generate Function
def generate_playlist():
    playlist_type = playlist_var.get()
    try:
        count = int(num_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    if playlist_type not in playlists:
        messagebox.showwarning("Oops!", "Please choose a playlist type.")
        return

    songs = playlists[playlist_type]
    if count > len(songs):
        messagebox.showerror(
            "Too Much!", f"Only {len(songs)} songs available.")
        return

    chosen = random.sample(songs, count)
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, "\n".join(
        f"{i+1}. {song}" for i, song in enumerate(chosen)))


# Generate Button
tk.Button(root, text="🎧 Generate Playlist",
          command=generate_playlist).pack(pady=10)


# Run the app
root.mainloop()
