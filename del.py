import tkinter
from tkinter import ttk


def clicked(event):
    event.x = event.x + 1
    label1.configure(text=f'Button was clicked {event.x} times!!!')


windows = tkinter.Tk()
windows.title("My Application")
label = tkinter.Label(windows, text="Hello World")
label.grid(column=0, row=0)
label1 = tkinter.Label(windows)
label1.grid(column=0, row=1)
custom_button = tkinter.ttk.Button(windows, text="Click on me")

custom_button.bind("<Button-1>", clicked)
custom_button.grid(column=1, row=0)
windows.mainloop()