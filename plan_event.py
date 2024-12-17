import tkinter as tk
from tkinter import messagebox


default_font = ("Arial", 20)

window = tk.Tk()
window.title(" Event Planner")
window.geometry("600x850")

label = tk.Label(window, 
                 text="Plan Your Event",
                 fg="blue",
                 font=default_font,).pack()

label = tk.Label(window, 
                 text="Enter the Event Name:",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

event_name = tk.Entry(window, 
                 font=default_font,
                 width=18)
event_name.pack()


label = tk.Label(window, 
                 text="Select Preferences:",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

check_include_catering = tk.IntVar()
checkbox_catering = tk.Checkbutton(
    window, text="Include Catering", variable=check_include_catering).pack(anchor="w")

check_provide_music = tk.IntVar()
checkbox_provide_music = tk.Checkbutton(
    window, text="Provide Music", variable=check_provide_music).pack(anchor="w")

check_enable_online_streaming = tk.IntVar()
checkbox_online_streaming = tk.Checkbutton(
    window, text="Enable Online Streaming", variable=check_enable_online_streaming).pack(anchor="w")

method = tk.StringVar(value="None")


label = tk.Label(window, 
                 text="Select Event Type:",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

wedding = tk.Radiobutton(window, font=("arial", 10), text="Wedding", 
                           value="Wedding", variable=method)
wedding.pack(anchor="w")

Conference = tk.Radiobutton(window, font=("arial", 10), text="Conference", 
                     value="Conference", variable=method)
Conference.pack(anchor="w")

birthday_party = tk.Radiobutton(window, font=("arial", 10), text="Birthday Party", 
                       value="Birthday Party", variable=method)
birthday_party.pack(anchor="w")


label = tk.Label(window, 
                 text="Number of Guests:",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

guest_scale = tk.Scale(window, from_=10, 
                 to=450,
                 length=400,
                 label="set the volume",
                 orient="horizontal",
                 tickinterval=50)

guest_scale.pack()


label = tk.Label(window, 
                 text="Select Event Theme:",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

event_theme = tk.Listbox(window, width=25, height=8,)
event_theme.pack()

event_theme.insert(1, "Modern")
event_theme.insert(2, "Classic")
event_theme.insert(3, "Rustic")
event_theme.insert(4, "Futuristic")
print(f"Current active: {event_theme.get(tk.ACTIVE)}")
event_theme.select_set(0)


def submit_btn():
    event_listbox = event_theme.get(tk.ACTIVE)
    event_name_data = event_name.get()
    genres = []
    if check_include_catering.get():
        genres.append("Include Catering")
    if check_provide_music.get():
        genres.append("Provide Music")
    if check_enable_online_streaming.get():
        genres.append("Enable Online Streaming")
    event_type = method.get()
    guest_number = guest_scale.get()


    # Prepare data for the messagebox
    genres_text = ", ".join(genres) if genres else "None"
    messagebox.showinfo("Event Summary",
                        f"Event Name: {event_name_data}\n"
                        f"Event Preferences: {genres_text}\n"
                        f"Event Type: {event_type}\n"
                        f"Number of Guests: {guest_number}\n"
                        f"Event Theme: {event_listbox}")
    
def reset_btn():
    event_name.delete(0, tk.END)

    check_enable_online_streaming.set(0)
    check_include_catering.set(0)
    check_provide_music.set(0)

    method.set("Something")

    guest_scale.set(0)

    event_theme.select_clear(0,tk.END)

    

submit_button = tk.Button(window, text="Submit", bg="green", fg="white", command=submit_btn)
submit_button.pack()

reset_button = tk.Button(window, text="Reset", bg="red", fg="white", command=reset_btn)
reset_button.pack()


window.mainloop()