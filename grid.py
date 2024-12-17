from tkinter import *



window = Tk()

first_name_label = Label(window, text="First Name: ", 
                         bg="orange").grid(row=0, column=0)
first_name_label = Entry(window).grid(row=0, column=1)
first_name_btn = Button(window,text="Click Me").grid(row=0, column=2)

last_name_label = Label(window, text="Last Name: ", 
                         bg="pink").grid(row=1, column=0)
last_name_label = Entry(window).grid(row=1, column=1)

submit_buttun = Button(window, text="Submit", width=30).grid(
                        row=2, column=0, columnspan=3)


window.mainloop()