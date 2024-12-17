from tkinter import *


def check():
    value = text.get('1.0','10.0')
    print(value)

window = Tk()
text = Text(window,
            font=('Courier New', 24),
            height=5, 
            width=30
)
text.pack()

btn = Button(window, text='check', command=check)
btn.pack()

window.mainloop()