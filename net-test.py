#!/usr/bin/python3

# Send UDP data

import socket

# address = input('address? ')
address = '127.0.0.1'
# port = int(input('port? '))
port = 8887
# message = input('message (hex)? ')
message = 'ff'

message = '000000' + message

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((address, port))
sock.sendto(bytes.fromhex(message), (address, port))

f = open('TESTFILE.BIN', 'wb')

data = sock.recv(4096).hex()
data = [data[i:i+2] for i in range(0, len(data), 2)]

print(data)
print(data[-1])
f.write(bytes.fromhex(data[-1]))
