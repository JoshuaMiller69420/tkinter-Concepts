from tkinter import *
from tkinter import ttk
import tkinter as tk

window = Tk()
tab_changes = 0
#def clicked(event):
#    event.x = event.x + 1
#    hi.configure(tab_changes += 1)


window.geometry("400x400")
scary_img = tk.PhotoImage(file="./resources/1.png")
t1 = tk.PhotoImage(file="./resources/1.png")
t2 = tk.PhotoImage(file="./resources/2.png")
t3 = tk.PhotoImage(file="./resources/3.png")
t4 = tk.PhotoImage(file="./resources/4.png")
t5 = tk.PhotoImage(file="./resources/5.png")
t6 = tk.PhotoImage(file="./resources/6.png")

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
tab4 = Frame(notebook)
tab5 = Frame(notebook)
tab6 = Frame(notebook)

 
notebook.add(tab1, text="First Tab")
notebook.add(tab2, text="Second Tab")
notebook.add(tab3, text="Third Tab")
notebook.add(tab4, text="Forth Tab")
notebook.add(tab5, text="Fifth Tab")
notebook.add(tab6, text="Sixth Tab")


Label(tab1, image=t1).pack()
Label(tab2, image=t2).pack()
Label(tab3, image=t3).pack()
Label(tab4, image=t4).pack()
Label(tab5, image=t5).pack()
Label(tab6, image=t6).pack()

Label(window, text=tab_changes).pack()


notebook.pack(expand=True, fill="both")

#if tab_changes == 1000:




window.mainloop()