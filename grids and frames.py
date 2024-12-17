from tkinter import *



window = Tk()
window.geometry("500x500")

frame_left = Frame(window, bg="green", 
                   width=200, height=200)
frame_left.grid(row=0, column=0)
frame_left.grid_propagate(False)

frame_right = Frame(window, bg="purple", 
                    width=200, height=200)
frame_right.grid(row=0, column=1)
frame_right.grid_propagate(False)



first_name_label = Label(window, text="First Name: ", 
                         bg="orange").grid(row=0, column=0)

first_name_label = Entry(window).grid(row=0, column=1)
first_name_btn = Button(window,text="Click Me").grid(row=0, column=2)

last_name_label = Label(window, text="Last Name: ", 
                         bg="pink").grid(row=0, column=1)
last_name_entry = Entry(window).grid(row=0, column=1)

submit_buttun = Button(window, text="Submit", width=30).grid(
                        row=1, column=0, columnspan=2)


window.mainloop()