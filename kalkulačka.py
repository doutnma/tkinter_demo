import tkinter as tk

window = tk.Tk()
window.geometry("100x100")
window.title("Kalkulačka")

entry1 = tk.Entry(
    width=15,
)
entry1.grid(row=0, column=1, columnspan=3)

def get_user_1():
    entry1.insert(tk.END, "1")
def get_user_2():
    entry1.insert(tk.END, "2")
def get_user_3():
    entry1.insert(tk.END, "3")
def get_user_4():
    entry1.insert(tk.END, "4")
def get_user_5():
    entry1.insert(tk.END, "5")
def get_user_6():
    entry1.insert(tk.END, "6")
def get_user_7():
    entry1.insert(tk.END, "7")
def get_user_8():
    entry1.insert(tk.END, "8")
def get_user_9():
    entry1.insert(tk.END, "9")
def get_user_0():
    entry1.insert(tk.END, "0")
def get_user_nasobeni():
    entry1.insert(tk.END, "*")
def get_user_deleni():
    entry1.insert(tk.END, "/")
def get_user_plus():
    entry1.insert(tk.END, "+")
def get_user_minus():
    entry1.insert(tk.END, "-")
def get_user_desetinne_cislo():
    entry1.insert(tk.END, ".")
def get_user_rovna_se():
    user_input = entry1.get()
    entry1.delete(0, tk.END)
    values = eval(user_input)
    entry1.insert(tk.END,values)
def get_user_smazani():
    entry1.delete(0, tk.END)

button_1 = tk.Button(
    text="1",
    fg="green",
    width=5,
    height=2,
    command=get_user_1
)
button_2 = tk.Button(
    text="2",
    fg="green",
    width=5,
    height=2,
    command=get_user_2
)
button_3 = tk.Button(
    text="3",
    fg="green",
    width=5,
    height=2,
    command=get_user_3
)
button_4 = tk.Button(
    text="4",
    fg="green",
    width=5,
    height=2,
    command=get_user_4
)
button_5 = tk.Button(
    text="5",
    fg="green",
    width=5,
    height=2,
    command=get_user_5
)
button_6 = tk.Button(
    text="6",
    fg="green",
    width=5,
    height=2,
    command=get_user_6
)
button_7 = tk.Button(
    text="7",
    fg="green",
    width=5,
    height=2,
    command=get_user_7
)
button_8 = tk.Button(
    text="8",
    fg="green",
    width=5,
    height=2,
    command=get_user_8
)
button_9 = tk.Button(
    text="9",
    fg="green",
    width=5,
    height=2,
    command=get_user_9
)
button_0 = tk.Button(
    text="0",
    fg="green",
    width=5,
    height=2,
    command=get_user_0
)
button_plus = tk.Button(
    text="+",
    fg="blue",
    width=5,
    height=2,
    command=get_user_plus
)
button_minus = tk.Button(
    text="-",
    fg="blue",
    width=5,
    height=2,
    command=get_user_minus
)
button_nasobeni = tk.Button(
    text="*",
    fg="blue",
    width=5,
    height=2,
    command=get_user_nasobeni
)
button_deleni = tk.Button(
    text="/",
    fg="blue",
    width=5,
    height=2,
    command=get_user_deleni
)
button_rovna_se = tk.Button(
    text="=",
    fg="blue",
    width=5,
    height=2,
    command=get_user_rovna_se
)
button_smazani = tk.Button(
    text="AC",
    fg="blue",
    width=5,
    height=2,
    command=get_user_smazani
)
button_desetinne_cislo = tk.Button(
    text=".",
    fg="blue",
    width=5,
    height=2,
    command=get_user_desetinne_cislo
)

button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=1, column=3)
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)
button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)
button_9.grid(row=3, column=3)
button_0.grid(row=4, column=1)
button_desetinne_cislo.grid(row=4, column=3)
button_smazani.grid(row=0, column=4)
button_plus.grid(row=1, column=4)
button_minus.grid(row=2, column=4)
button_nasobeni.grid(row=3, column=4)
button_rovna_se.grid(row=4, column=2)
button_deleni.grid(row=4, column=4)

window.mainloop()