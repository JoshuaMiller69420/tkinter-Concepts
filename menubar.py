from tkinter import *
import random

def openfile():
    print("You opned the file!")


def savefile():
    print("You saved the file!")


def editfile():
    print("You edited the file!")


def annoy():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    for i in range(1000):
        new_window = Tk()
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        new_window.geometry(f"200x200+{x}+{y}")


window = Tk()
window.geometry("400x400")


toplevel_menubar = Menu(window)
window.config(menu=toplevel_menubar)

filemenu = Menu(toplevel_menubar, tearoff=0)
toplevel_menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)


editmenu = Menu(toplevel_menubar, tearoff=0)
toplevel_menubar.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Edit", command=editfile)


chaosmenu = Menu(toplevel_menubar, tearoff=0)
chaosmenu.add_command(label="annoy", command=annoy)
toplevel_menubar.add_cascade(label="Chaos", menu=chaosmenu)


window.mainloop()