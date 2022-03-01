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

window.mainloop()