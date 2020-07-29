#!/usr/bin/python3

# https://github.com/cadenmr/datatape-comm
# https://github.com/cadenmr/datatape

# This script communicates with the datatape FPGA project for storing high-density
# data on S-VHS tapes. (See repos above)

# This script is designed and tested under Linux. Use under other OSes is
# untested.

# If you find a bug, please report it under the correct repo.

# Have fun!

if not __name__ == "__main__":
    raise RuntimeError("This script is intended to be run directly")

import socket
import os

valid_run_modes = ('r', 'w')

output_filename = 'data.bin'
socket_port = 8887
socket_address = input('IP of FPGA? ')
run_mode = None

while run_mode not in valid_run_modes:
    run_mode = input('Run Mode (r/w)? ')

# Read Data Mode
if run_mode == 'r':

    try:
        os.remove(output_filename)
    except FileNotFoundError:
        pass

    output = open(output_filename, 'wb')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto(bytes.fromhex(), (socket_address, socket_port))


# Write Data Mode
elif run_mode == 'w':
    raise NotImplementedError

else:
    raise ValueError('run_mode was not r or w (how????)')
