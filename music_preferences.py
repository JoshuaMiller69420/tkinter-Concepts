import tkinter as tk
from tkinter import messagebox


default_font = ("Arial", 20)

window = tk.Tk()
window.title(" My Music Preferences")
window.geometry("600x600")

label = tk.Label(window, 
                 text="Welcome to My Music Preferences!",
                 fg="purple",
                 font=default_font,).pack()

label = tk.Label(window, 
                 text="Who is your favorite atist or band?",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

fav_band = tk.Entry(window, 
                 font=default_font,
                 width=18)
fav_band.pack()
#fav_band.insert(0, "Band Here")

label = tk.Label(window, 
                 text="Select your favorite music genres:",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

check_rock = tk.IntVar()
checkbox_rock = tk.Checkbutton(
    window, text="Rock", variable=check_rock).pack(anchor="w")

check_pop = tk.IntVar()
checkbox_pop = tk.Checkbutton(
    window, text="Pop", variable=check_pop).pack(anchor="w")

check_jazz = tk.IntVar()
checkbox_jazz = tk.Checkbutton(
    window, text="Jazz", variable=check_jazz).pack(anchor="w")

method = tk.StringVar(value="None")

label = tk.Label(window, 
                 text="Choose your preferred listening method:",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

streaming = tk.Radiobutton(window, font=("arial", 10), text="Streaming", 
               value="Streaming", variable=method)
streaming.pack(anchor="w")
cds = tk.Radiobutton(window, font=("arial", 10), text="CDs", value="CDs", variable=method)
cds.pack(anchor="w")
vinyl = tk.Radiobutton(window, font=("arial", 10), text="Vinyl", value="Vinyl", variable=method)
vinyl.pack(anchor="w")

def submit_btn():
    favorite_artist_data = fav_band.get()
    genres = []
    if check_rock.get():
        genres.append("Rock")
    if check_pop.get():
        genres.append("Pop")
    if check_jazz.get():
        genres.append("Jazz")
    listening_method = method.get()

    # Prepare data for the messagebox
    genres_text = ", ".join(genres) if genres else "None"
    messagebox.showinfo("Music Preferences",
                        f"Favorite Artist/Band: {favorite_artist_data}\n"
                        f"Favorite Genres: {genres_text}\n"
                        f"Preferred Listening Method: {listening_method}")

    

button = tk.Button(window, text="Submit", bg="blue", fg="white", command=submit_btn)
button.pack()


window.mainloop()