import tkinter as tk
from tkinter import messagebox

def get_user_input():
    user_input = entry1.get()
    if user_input == "Spráťa":
        messagebox.showinfo("Pozdráveček", "Nazdar Spráťo " + "!!!")
    elif user_input == "Vojta Neymar 4D":
        messagebox.showinfo("Pozdráveček", "Čaute tiktokéři " + "!!!")
    elif user_input == "Jiří Š.":
        messagebox.showinfo("Pozdráveček", "Class diagram, Sekvenční, Use Case, Statechart " + "!!!")
    else:
        messagebox.showinfo("Pozdrav", "Nazdárek " + user_input + "!!!")

window = tk.Tk()
window.geometry("100x100")
window.title("Testík")

"""
Label
Entry
Button
Text
"""

label1 = tk.Label(
    text="Moje aplikace",
    background="black",
    foreground="white",
    width=10,
    height=1
)

label1.grid(row=0, column=0, columnspan=2)

entry1 = tk.Entry(
    width=20
)

#sticky=""

entry1.grid(row=2, column=1)
button1 = tk.Button(
    text="Naklikej to sem!!!",
    bg="black",
    fg="green",
    width=21,
    height=2,
    command=get_user_input
)

button1.grid(row=3, column=1)

window.mainloop()