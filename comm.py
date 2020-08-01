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
run_mode = None

socket_port = 8887
socket_address = input('IP of FPGA? ')

# Open a socket for the FPGA
fpga_device = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
fpga_device.bind((socket_address, socket_port))  # Bind the socket

while run_mode not in valid_run_modes:
    run_mode = input('Run Mode (r/w)? ')

# Read Data Mode
if run_mode == 'r':

    output_filename = input('Output filename? ')

    # Attempt to remove an old dump with the same filename
    try:
        os.remove(output_filename)
    except FileNotFoundError:
        pass

    # Open a file for binary writing
    output = open(output_filename, 'wb')

    # Open the FPGA for reading
    fpga_device.sendto(bytes.fromhex('01000000'), (socket_address, socket_port))  # TODO: Set up FPGA commands
    print('FPGA initialized')

# Write Data Mode
elif run_mode == 'w':

    input_filename = input('File to write? ')
    print('Please begin recording on the VCR')
    input('Press enter to begin writing data')
    print('----------------------------------')

    print('File opened')

    # Open the FPGA for writing
    fpga_device.sendto(bytes.fromhex(''), (socket_address, socket_port))
    print('FPGA initialized')



else:
    raise ValueError('run_mode was not r or w (how????)')
