from tkinter import *
from tkinter import filedialog

def save_text():
    writer = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text Files", "*.txt")]
                                         )
    if writer:
        with open(writer, "w") as writer:
            writer.write(text_area.get("1.0", END))
        print(f"Text saved to {writer}")


window = Tk()
window.geometry("400x400")
window.geometry = (0, 0)

text_area = Text(window, width=10, height=10,)

Button(window, text="Save Text", command=save_text).pack()


window.mainloop()