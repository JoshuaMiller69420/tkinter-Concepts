from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
 
 
def changebg():
    color = colorchooser.askcolor()
    print(color)
    spaceship_color.config(bg=color[1])
 
 
def message():
    value = alien_text.get(1.0, "2.50")
    print(f"Alien Message: {value}")



 
 
window = Tk()
window.geometry("600x550")
window.title("Alien Invader HQ Control Panel")
 
icon = PhotoImage(file="./resources/R.png")
window.iconphoto(True, icon)
 
Top_Frame = Frame(window, width="250",height="250")
Top_Frame.pack()

Label(Top_Frame, image=icon).pack()
 

Middle_Frame = Frame(window, width="100", height="100")
Middle_Frame.pack(anchor=W)
 
spaceship_color = Label(
Middle_Frame, bg="gray", width=20, height=5)
spaceship_color.grid(row=0, column=0)
 
button = Button(Middle_Frame, text="Change Spaceship Color",
                command=changebg)
button.grid(row=0, column=0)
 
alien_text = Text(Middle_Frame, width=40, height=5)
alien_text.grid(row=0, column=1)

text = Button(Middle_Frame, text="Send Message", command=message)
text.grid(row=1, column=1, pady=10)

Button(Middle_Frame, text="Upload Secret File").grid(row=2, column=0)

Label(Middle_Frame, text="Select Invasion Plan:").grid(row=2, column=1, pady=10)

listbox = Listbox(Middle_Frame, width=20, height=4)
listbox.grid(row=3,column=1)

listbox.insert(1, "Plan A: Earth Takeover")
listbox.insert(2, "Plan B: Moon Dominatoin")
listbox.insert(3, "Plan C: Mars Colonization")

def launch_plan():
    lsitbox = listbox.get(ACTIVE)
    response = messagebox.askyesno("Confirm Launch", f"Are you sure you want to launch{listbox}")
    print(response)
    if response:
        print("We're doing this!")
    else:
        print("User wimped out")

Button(Middle_Frame, text="Launch Plan", command=launch_plan).grid(row=4, column=1, pady=10)


Bottom_Frame = Frame(window, bg="white", width=250, height=250)
Bottom_Frame.pack()

Label(Bottom_Frame, text="Balls", bg="white", width=85, relief=RAISED).pack()

Button(Bottom_Frame, text="Exit", width=3, height=1).pack()


 
window.mainloop()