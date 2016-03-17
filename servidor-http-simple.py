#!/usr/bin/python

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

machine = socket.gethostname()
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    print 'Waiting for connections'
    (recvSocket, address) = mySocket.accept()
    Num = str(random.randint(1,60000))
    ip = address[0]
    port = address[1]
    print 'HTTP request received:'
    print recvSocket.recv(1024)
    html = "<html><body><h1>Hello Word!</h1>"
    html += "<p>Hola <a href=http://localhost:1234/"+Num+"> Dame otra pagina</a>"
    html += "</p></body></html>"
    recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                    html +
                    "\r\n")
    recvSocket.close()
