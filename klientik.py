import socket, threading
import tkinter as tk
import time

def prichozi_zpravy(connection: socket.socket):
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                print(msg.decode())
            else:
                connection.close()
                break
        except Exception as e:
            print(f'Error handling message from server: {e}')
            connection.close()
            break

def login():
    hostval = ip.get()
    portval = port.get()
    try:
        s.connect((hostval, int(portval)))
        threading.Thread(target=prichozi_zpravy, args=[s]).start()
        print('Připojeno do chatovací místnosti')

        ip.grid_remove()
        labelIP.grid_remove()
        port.grid_remove()
        labelPort.grid_remove()
        enterLogin.grid_remove()

        labelName.grid_remove()
        name.grid_remove()

        errMsg = tk.Label(text="Připojeno !")

        time.sleep(1)
        errMsg.grid_remove()

        messageText.grid(sticky="N")
        sendButton.grid(sticky="S")

    except Exception as e:
        print(f'Error při připojování k serveru {e}')
        ip.delete(0, tk.END)
        port.delete(0, tk.END)
        errMsg = tk.Label(text="Error při připojování k serveru")
        errMsg.grid(sticky="N")

def send():
    msg = messageText.get()
    s.send(msg.encode())

window = tk.Tk()
window.geometry("400x300")
window.title("Četík")

s = socket.socket()

labelIP = tk.Label(text="Zadejte IP adresu serveru")
ip = tk.Entry()

labelPort = tk.Label(text="Zadejte Port")
port = tk.Entry()

labelIP.grid(sticky="S")
ip.grid(sticky="S")

labelPort.grid(sticky="S")
port.grid(sticky="S")

labelName = tk.Label(text="Přezdívka")
name = tk.Entry()

enterLogin = tk.Button(text="Připojit", command=login)
enterLogin.grid(sticky="S")

messageText = tk.Entry()
sendButton = tk.Button(text="Odeslat", command=send)

window.mainloop()

host = input(str('Host / IP : '))
port = input(str('Port : '))

try:
    s.connect((host, int(port)))
    threading.Thread(target=prichozi_zpravy, args=[s]).start()
    print('Připojeno do chatovací místnosti')
    while True:
        msg = input('>>')
        if msg == 'q_app_q_69':
            break
        s.send(msg.encode())
        s.close()

except Exception as e:
    print(f'Error při připojování k serveru {e}')
    s.close()