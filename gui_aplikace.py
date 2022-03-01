import tkinter as tk
tk.Tk()

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
    foreground="white"
)

label1.pack()

entry1 = tk.Entry(
    width=20,
)
entry1.pack()

button1 = tk.Button(
    text="Klik!!!",
    bg="black",
    fg="green",
    width=20,
    height=2
)

button1.pack()

window.mainloop()