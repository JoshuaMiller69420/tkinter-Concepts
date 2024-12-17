#checkboxes!
import tkinter as tk

def grade_submission():
    valveta = check_valveta.get()
    garbage = check_kraft.get()
    if valveta ==1 and garbage == 0:
        label_outcome.config(text="You are 100% correct!")
    elif valveta == 0 and garbage == 1:
        label_outcome.config(text="You are dead wrong!")
    elif valveta == 1 and garbage == 1:
        label_outcome.config(text="You are partially correct.")
    else:
        label_outcome.config(text="No box picked, try again.")


window = tk.Tk()
window.title("Mac and Cheese Survey")
window.geometry("500x500")
#thumbs_up = tk.PhotoImage(file="./resources/thumbs_up.jpg")

#variable to hold the state of the checkbox
check_kraft = tk.IntVar()
checkbox_kraft = tk.Checkbutton(
    window, text="Kraft mac & cheese is good.", variable=check_kraft)
checkbox_kraft.pack()

check_valveta = tk.IntVar()
checkbox_valveta = tk.Checkbutton(
    window, text="Valveta is good.", variable=check_valveta)
checkbox_valveta.pack()

button_submit = tk.Button(window, text="Submit", command=grade_submission)
button_submit.pack()

label_outcome = tk.Label(window, text="Please submit your response")
label_outcome.pack()

window.mainloop()