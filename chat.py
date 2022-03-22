import socket
import tkinter as tk

s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = 'DST22812'
port = 2205

s.connect((host, port))
msg = s.recv(1024)
print(msg.decode('ascii'))
s.close()

def get_user_input():
    msg_back = entry1.get()
    label1 = tk.Label(
        text=msg_back,
        bg="black",
        fg="white",
        width=20,
        height=1
    )
    label1.grid(row=1, column=1)

window = tk.Tk()
window.geometry("100x100")
window.title("Četík")

entry1 = tk.Entry(
    width=20
)

entry1.grid(row=0, column=1)

send_button = tk.Button(
    text="Enter",
    bg="white",
    fg="black",
    width=5,
    height=2,
    command=get_user_input
)

send_button.grid(row=0, column=3)

window.mainloop()