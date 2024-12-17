import tkinter as tk
click = 0

def on_button_click():
    global click
    click += 1
    print(f"Button was clicked {click}")
    label.config(text=click)



default_font = ("Arial", 20, "bold")
window = tk.Tk()

window.title("Edward Robinson Clicker Counter")
window.geometry("600x400")


icon = tk.PhotoImage(file="./resources/edward_robinson100.png")
window.iconphoto(True, icon)

#change the backgroun color of the window
window.config(bg="green")

#create a label
label = tk.Label(window, 
                text= "Click the Edward Button",
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
                   text="Edward Button", 
                   font = default_font,
                   command = on_button_click,
                   activebackground="red",
                   activeforeground="green"
                   )

button.pack()

window.mainloop()
