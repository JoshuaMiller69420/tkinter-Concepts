from tkinter import *
from tkinter import filedialog

def openfile():
    fle_name = filedialog.askopenfilenames(
        title="Open awesome file",
        filetypes = (("Comma Seperated Values", "*.csv"), 
                     ("Text Files", "*.txt"), 
                     ("Json Files", "*.json")
                     )
    )
    if fle_name:
        with open(fle_name,"r") as file:
            content = file.read()
            print(content)


def savefile():
    writer = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text Files", "*.txt"), 
                                                    ("Json Files", "*.json"),
                                                    ("Comma Seperated Values", "*.csv")]
                                         )
    if writer:
        with open(writer, "w") as writer:
            writer.write(text_area.get("1.0", END))
        print(f"Text saved to {writer} successfully.")


window = Tk()
window.geometry("500x500")


toplevel_menubar = Menu(window)
window.config(menu=toplevel_menubar)

filemenu = Menu(toplevel_menubar, tearoff=0)
toplevel_menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)


editmenu = Menu(toplevel_menubar, tearoff=0)
toplevel_menubar.add_cascade(label="Edit", menu=editmenu)


text_area = Text(window,
            font=('Courier New', 24)
)
text_area.pack()

window.mainloop()