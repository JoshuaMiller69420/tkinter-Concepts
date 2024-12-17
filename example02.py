import tkinter as tk
import time

def submit():
    ssn = ssn_en.get()
    name = name_en.get() #gets teh text from our entry
    print(f"We got the ssn! {ssn}")
    print(f"we got the name! {name}")
    label.config(text = "THANKS FOR THE SSN!", image=img)
    #entry_name.config(state=tk.DISABLED)


    #quit()

#create a window
default_font = ("Arial", 20, "bold")

window = tk.Tk()
window.title("Social Sacurity Scam App")
window.geometry("700x600")

img = tk.PhotoImage(file="./resources/troll_face.png")

icon = tk.PhotoImage(file="./resources/indian_guy.png")
window.iconphoto(True, icon)

label = tk.Label(window, 
                text="Please entah your social security numberr and your name in thu bock below.",
                font = default_font,
                foreground="black",
                background="brown",
                image = icon,
                compound = "top",
                bd=20,
                relief=tk.RAISED,
                padx=15,
                pady=25
                )
label.pack(pady=20)

ssn_en = tk.Entry(window, 
                 font=default_font,
                 width=15,
                 show="*")
name_en = tk.Entry(window, 
                 font=default_font,
                 width=15)
ssn_en.pack()
name_en.pack()


#set default text
ssn_en.insert(0, "555-55-5555")
name_en.insert(0, "Name Here")

submit = tk.Button(window, 
                   text="Submit", 
                   font = default_font,
                   command = submit,
                   width=6
                   )
submit.pack()

window.mainloop()