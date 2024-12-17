import tkinter as tk
from tkinter import messsagebox

def show_message():
    response = messsagebox.askyesno("Yes or No?", "Are we really doing this?")
    print(response)
    if response:
        print("We're doing this!")
    else:
        print("User wimped out")

window = tk.TK()
window.title("Message Box Example")
window.geometry("400x300")

button = tk.Button(window, 
                   text="Show Message Box", 
                   command=show_message)
button.pack()

window.mainloop()