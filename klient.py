import socket

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