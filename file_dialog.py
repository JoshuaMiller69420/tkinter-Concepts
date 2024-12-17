from tkinter import *
from tkinter import filedialog

def open_file():
    fle_name = filedialog.askopenfilenames(
        title="Open awesome file",
        filetypes = (("Comma Seperated Values", "*.csv"), 
                     ("Excel", "*.xlxs"), 
                     ("All Files", "*.*")
                     )
    )
    if fle_name:
        with open(fle_name,"r") as file:
            content = file.read()
            print(content)

    print(fle_name)


window = Tk()
window.geometry("200x100")
Button(window, text="Open", command=open_file).pack()


window.mainloop()