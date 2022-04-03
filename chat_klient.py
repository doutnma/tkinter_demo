import socket, threading
import tkinter as tk
from tkinter import *
import time
from tkinter import END
global nick

def prichozi_zpravy(connection: socket.socket):
    text.grid(sticky="W")
    text.configure(state='disabled')
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                print(msg.decode())
                text.configure(state='normal')
                aaa = str(msg.decode())
                text.insert(END, aaa + '\n')
                text.configure(state='disabled')
            else:
                connection.close()
                break
        except Exception as e:
            print(f'Error: {e}')
            connection.close()
            break
def login():
    hostval = ip.get()
    portval = port.get()
    prezdivka = name.get()

    if prezdivka != "":
        try:
            s.connect((hostval, int(portval)))
            threading.Thread(target=prichozi_zpravy, args=[s]).start()
            print('Připojeno do chatíku')
            ip.grid_remove()
            labelIP.grid_remove()
            port.grid_remove()
            labelPort.grid_remove()
            enterLogin.grid_remove()
            labelName.grid_remove()
            name.grid_forget()
            errMsg = tk.Label(text="Připojeno!!!")
            errMsg.grid(sticky="W")
            time.sleep(1)
            errMsg.grid_remove()
            text.configure(state='disabled')
            messageText.grid(sticky="N")
            sendButton.grid(sticky="S")
        except Exception as e:
            print(f'Error{e}')
            ip.delete(0, tk.END)
            port.delete(0, tk.END)
            errMsg=tk.Label(text="Error")
            errMsg.grid(sticky="W")
            time.sleep(1)
            errMsg.grid_remove()
    else:
        errMsg2 = tk.Label(text="Vaše přezdívka:")
        errMsg2.grid(sticky="W")
        time.sleep(1)
        errMsg2.grid_remove()

def sendMsg():
    text.configure(state='normal')
    msg = messageText.get()
    s.send(msg.encode())
    if msg != "":
        msg1 = "Moje zpráva - {}".format(msg)
        text.insert(END, msg1 + '\n')
        messageText.delete(0, tk.END)
    text.configure(state='disabled')

window = tk.Tk()
window.geometry("400x300")
window.title("Četík")
s = socket.socket()

labelIP=tk.Label(
    text = "Zadejte IP adresu serveru",
    width = 20,
    fg="red",
    bg="black"
)
ip=tk.Entry()

labelPort=tk.Label(
    text = "Zadejte Port",
    width=20,
    fg="red",
    bg="black"
)
port=tk.Entry()

labelIP.grid(row=1, column=0)
ip.grid(row=1, column=2)

labelPort.grid(row=2, column=0)
port.grid(row=2, column=2)

labelName=tk.Label(
    text = "Přezdívka",
    fg="red",
    bg="black",
    width=20
)
name=tk.Entry()

labelName.grid(row=3, column=0)
name.grid(row=3, column=2)

enterLogin=tk.Button(text = "Připojit se do četíku", command=login)
enterLogin.grid(row=4, column=2)

messageText = tk.Entry(
    width=10,
)

sendButton = tk.Button(
    text="Poslat",
    command=sendMsg,
    width=10
)

text = tk.Text(width=60, height=10)

window.mainloop()