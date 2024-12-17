from tkinter import *
from tkinter import colorchooser

def changebg():
    color = colorchooser.askcolor()
    print(color)
    # color[0] is rgb
    #color[0] is hex
    window.config(bg=color[1])

window = Tk()
window.geometry("400x400")

btn = Button(text = "Change bg", command=changebg)
btn.pack()


window.mainloop()