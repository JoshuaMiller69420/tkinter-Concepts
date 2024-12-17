#a fframe is a rectangular container to gruop and hold widgets
from tkinter import *

window = Tk()
window.geometry("400x400")

frame = Frame(window, bg="yellow")
frame.pack(side=LEFT)

Button(frame, text="W", width=3).pack(side=TOP)
Button(frame, text="A", width=3).pack(side=LEFT)
Button(frame, text="S", width=3).pack(side=LEFT)
Button(frame, text="D", width=3).pack(side=LEFT)
Button(frame, text="X", width=3).pack(side=BOTTOM)



window.mainloop()