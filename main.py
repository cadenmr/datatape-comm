import multiprocessing
import socket
import os

import constants
import ethio

local_network_dev = (socket.gethostbyname(socket.gethostname()), 1234)
dest_network_dev = ('192.168.1.128', 1234)
tx_packet_size = 384
rx_udp_bufsize = 1024


def _mode_oob():
    raise ValueError('mode selection value out of bounds')


# TODO: REPLACE THIS DIRTY MENU CODE WITH A GUI
def menu():

    valid_modes = (1, 2)
    mode_selection = 0
    filename = None

    # Clear the screen on script start
    if os.name == 'posix':
        _ = os.system('clear')
    elif os.name == 'nt':
        _ = os.system('cls')
    else:
        raise OSError('unsupported OS')

    print('datatape\n\n1: write data to tape\n2: read data from tape\n')
    while mode_selection not in valid_modes:
        mode_selection = input('mode: ')
        try:
            mode_selection = int(mode_selection)
        except ValueError:
            pass

    if mode_selection == 1:
        filename = input('input file path: ')
    elif mode_selection == 2:
        filename = input('output file path: ')
    else:
        _mode_oob()

    return mode_selection, filename


if __name__ == '__main__':

    mode, file_path = menu()

    # Mode 1: Write to tape
    if mode == 1:
        with open(file_path, 'rb') as in_file:

            # TODO: Code this
            pass

    # Mode 2: Read from tape
    elif mode == 2:
        with open(file_path, 'wb') as out_file:

            # TODO: Code this
            pass

    else:
        _mode_oob()
