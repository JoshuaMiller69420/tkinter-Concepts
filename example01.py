# GUI - Graphical User Interphase
import tkinter as tk

def on_button_click():
    #img = tk.PhotoImage(file="./resources/edward_robinson100.png")
    print("Button was clicked!")
    label.config(text="EDWARD ROBINSON IS BETTER!!!", image=img)



default_font = ("Arial", 20, "bold")
window = tk.Tk()

img = tk.PhotoImage(file="./resources/edward_robinson100.png")

# Give the window a title
window.title("Edward Robinson Application")

# set the size of the window
window.geometry("600x400")

#change the icon in the top left
icon = tk.PhotoImage(file="./resources/garfield100.png")
window.iconphoto(True, icon)

#change the backgroun color of the window
window.config(bg="green")

#create a label
label = tk.Label(window, 
                text="Is garfield a sigma?",
                font = default_font,
                foreground="green",
                background="purple",
                image = icon,
                compound = "top",
                bd=20,
                relief=tk.RAISED,
                padx=15,
                pady=25
                )
#could shorthand foreground?/background with fg/bg

#label will not be there until we pack it
label.pack(pady=20)

#place a label in a spot
#label.place(x=0, y=0)

#button thingy
button = tk.Button(window, 
                   text="How about Edward?", 
                   font = default_font,
                   command = on_button_click,
                   activebackground="red",
                   activeforeground="green"
                   )

button.pack()

window.mainloop()
