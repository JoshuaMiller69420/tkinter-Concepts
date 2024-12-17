import tkinter as tk

window = tk.Tk()
window.title("Class President")
window.geometry("500x500")
font_info = font="Arial"

label_vote = tk.Label(text="Please make a selectoin for class president",
                      font=font_info)
label_vote.pack()
vote = tk.StringVar(value="Mr. Jason Klins")

tk.Radiobutton(window, font=font_info, text="Mr. Klins", 
               variable=vote, value="Mr. James Klins").pack()
tk.Radiobutton(window, font=font_info, text="James", 
               variable=vote, value="James Clark").pack()
tk.Radiobutton(window, font=font_info, text="Coby", 
               variable=vote, value="Coby Hughes").pack()
tk.Radiobutton(window, font=font_info, text="Kerry", 
               variable=vote, value="Kerry Sowers").pack()


def record_vote():
    label_vote.config(text=f"You voted for {vote.get()}")

tk.Button(window, text="submit", command=record_vote).pack()

window.mainloop()