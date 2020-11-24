#TCP server

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port =  444

#server ip address (host)
serversocket.bind(('10.211.55.4', port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print(f"received connection from {address}")

    message = "hello, thanks for connecting to server \r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()






