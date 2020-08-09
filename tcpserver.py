#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname
port = 4444

serversocket.bind(('', port))

serversocket.listen(7)

while True:
    clientsocket, address = serversocket.accept()

    print("Received connection from: %s" % str(address))

    message = "Hey buddy, You've been Successfully connected to the server" + "/r/n"

    clientsocket.send(message)
    clientsocket.close()

