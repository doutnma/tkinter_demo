import socket, threading
import logging
from datetime import datetime
import os
import sys

logname = datetime.now()

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

aktivni_users = []

def rozesilani_zprav(connection: socket.socket, address: str):
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                print(f' uživatel {address[0]}:{address[1]} napsal {msg.decode()}')
                logger.info(f'{address[0]}:{address[1]} - {msg.decode()}')
                msg_to_send = f'{address[0]}:{address[1]} - {msg.decode()}'
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
                if connection in aktivni_users:
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
print(' Adresa Serveríku: ', host)

port = 3304
print(' Portík: ', port)
s.bind((host, port))

logger.debug("Server je spuštěn")
logger.debug(f'Adresa serveru : {host}')
logger.debug(f'Port serveru : {port}')

while True:
    s.listen(10)
    socket_connection, address = s.accept()
    print(address, ' připojen')
    logger.info(f'{address[0]}:{address[1]} - připojen')
    hi = " {} připojen!".format(address)

    socket_connection.sendall(str.encode(hi))

    for client_conn in aktivni_users:
        try:
            client_conn.send(hi.encode())
        except Exception as e:
            print(f'Error při navazování spojení: {e}')
            logger.warning(f'Error při navazování spojení-{address[0]}:{address[1]}')
            if socket_connection in aktivni_users:
                socket_connection.close()
                aktivni_users.remove(socket_connection)
                logger.warning(f'Neaktivní uživatel byl odstraněn -{address[0]}:{address[1]}')
            break
    aktivni_users.append(socket_connection)
    threading.Thread(target=rozesilani_zprav, args=[socket_connection, address]).start()