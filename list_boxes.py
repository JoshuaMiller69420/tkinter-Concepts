import tkinter as tk


def add_character():
    item = entry.get().strip()
    if item and not item in listbox.get(0, tk.END):
        listbox.insert(tk.END, item)


def remove_selected():
    for_del = listbox.get(tk.ACTIVE)
    if for_del:
        listbox.delete(tk.ACTIVE)
        print(f"Deleted {for_del}")
        print(f"Current active: {listbox.get(tk.ACTIVE)}")


window = tk.Tk()
window.geometry("300x300")
window.title("Mario Characters")

listbox = tk.Listbox(window, width=25, height=8,)
listbox.pack()

listbox.insert(1, "Mario")
listbox.insert(2, "Luigi")
listbox.insert(3, "Princess Peach")
print(f"Current active: {listbox.get(tk.ACTIVE)}")
listbox.select_set(1)


label = tk.Label(text="Enter a character to add:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Add charcter", command=add_character)
button.pack()

button_del = tk.Button(window, text="Remove Selected", command=remove_selected)
button_del.pack()


window.mainloop()