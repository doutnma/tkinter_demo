import socket, threading

aktivni_users = []

def rozesilani_zprav(connection: socket.socket, address: str):
    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(f'{address[0]}:{address[1]} - {msg.decode()}')
                msg_to_send = f'Od {address[0]}:{address[1]} - {msg.decode()}'
                for client_conn in aktivni_users:
                    if client_conn != connection:
                        try:
                            client_conn.send(msg_to_send.encode())
                        except Exception as e:
                            print('Error broadcasting message: {e}')
                            if connection in aktivni_users:
                                connection.close()
                                aktivni_users.remove(connection)

            else:
                # Kontrola, zda-li je uživatel v aktivni_users
                if connection in aktivni_users:
                    # odstranění uživatele z aktivni_users
                    connection.close()
                    aktivni_users.remove(connection)
                break

        except Exception as e:
            print(f'Error při navazování spojení: {e}')
            if connection in aktivni_users:
                connection.close()
                aktivni_users.remove(connection)
            break

s = socket.socket()
host = socket.gethostname()
print(' Serverík běží na adrese : ', host)
port = 3302
print(' Portíček : ', port)
s.bind((host, port))

while True:
    s.listen()
    socket_connection, address = s.accept()
    print(address, ' Připojeno')
    hi = " {} se pripojil!".format(address)
    socket_connection.sendall(str.encode(hi))

    for client_conn in aktivni_users:
        try:
            client_conn.send(hi.encode())
        except Exception as e:
            print(f'Error při navazování spojení: {e}')
            if socket_connection in aktivni_users:
                socket_connection.close()
                aktivni_users.remove(socket_connection)
            break
    aktivni_users.append(socket_connection)
    threading.Thread(target=rozesilani_zprav, args=[socket_connection, address]).start()
