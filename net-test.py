#!/usr/bin/python3

# Send UDP data

import socket

address = input('address? ')
port = int(input('port? '))
message = input('message (hex)? ')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes.fromhex(message), (address, port))

