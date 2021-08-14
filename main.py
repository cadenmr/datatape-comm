import multiprocessing
import socket
import os

import constants
import ethio

local_network_dev = ('192.168.1.5', 1234)
dest_network_dev = ('192.168.1.5', 1234)
rx_udp_bufsize = 1024


def _mode_oob():
    raise ValueError('mode selection value out of bounds')


# Wait for a command acknowledge or tape write continue keyword
def _wait_for_fpga(s):
    while True:
        rx_d, rx_a = s.recvfrom(rx_udp_bufsize)
        if rx_a == local_network_dev[0]:
            if rx_d == constants.cmd_ack or rx_d == constants.tape_write_cont_kwd:
                break


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
    dest_dev = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_dev.bind(local_network_dev)

    # Mode 1: Write to tape
    if mode == 1:
        with open(file_path, 'rb') as in_file:

            print('sending file...')

            # send beginning of transmission
            dest_dev.sendto(constants.bot_kwd, dest_network_dev)
            # wait for FPGA to acknowledge command
            _wait_for_fpga(dest_dev)
            # send beginning of file
            dest_dev.sendto(constants.bof_kwd, dest_network_dev)

            first_packet = True
            last_packet = False
            while True:
                tx_d = in_file.read(constants.payload_size)

                if len(tx_d) < constants.payload_size:
                    last_packet = True

                # Select the appropriate prefix
                if first_packet and not last_packet:
                    tx_d = constants.fpof_kwd + tx_d
                    first_packet = False
                elif not first_packet and last_packet:
                    tx_d = constants.lpof_kwd + tx_d
                elif not first_packet and not last_packet:
                    tx_d = constants.inf_kwd + tx_d
                else:
                    raise ValueError(f'wut\n\n(first_packet, last_packet)\n{first_packet, last_packet}')

                # wait for the fpga to be ready before we send the next packet
                _wait_for_fpga(dest_dev)
                # send the packet
                dest_dev.sendto(tx_d, dest_network_dev)

                if last_packet:
                    dest_dev.sendto(constants.eof_kwd, dest_network_dev)
                    break

        dest_dev.sendto(constants.eot_kwd, dest_network_dev)
        print('done!')

    # Mode 2: Read from tape
    elif mode == 2:
        with open(file_path, 'wb') as out_file:

            # TODO: Code this
            pass

    else:
        _mode_oob()
