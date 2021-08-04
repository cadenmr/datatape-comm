# datatape_comm eth io lib

import socket
import multiprocessing

# TODO: Handle keyword input better
# TODO: import constants here?


class EthIO:
    def __init__(self, local_dev, dest_dev, udp_rx_bufsize, eof_kwd, eot_kwd):
        
        # local_dev = (local_ip, dest_port)
        # dest_dev = (dest_ip, dest_dev)
        
        self._dest_dev = dest_dev  # (dest_ip, dest_port)
        self._eof_kwd = eof_kwd
        self._eot_kwd = eot_kwd

        self._udp_rx_bufsize = udp_rx_bufsize
        
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind(local_dev)

        # set 10 second timeout
        socket.settimeout(10)

    def tx_control(self, data_queue):
        while True:

            if data_queue.empty():
                break

            tx_d = data_queue.get()
            self._sock.sendto(tx_d, self._dest_dev)

            try:
                rx_d = self._sock.recvfrom(self._udp_rx_bufsize)
            except socket.timeout:
                pass
            # TODO: check if received data matches the ack kwd

    def tx_data(self, data_pipe):
        while True:
            tx_d = data_pipe.recv()
            if not tx_d:
                print('eth_tx: recv "False", terminating')
                self._sock.sendto(self._eof_kwd, self._dest_dev)
                break
            self._sock.sendto(tx_d, self._dest_dev)
        self._sock.sendto(self._eot_kwd, self._dest_dev)

    '''
    method rx(data_pipe)
    
    this function takes in a multiprocessing.Pipe object
    and transmits all packets received from the dest_dev
    passed into the class initializer
    
    this function terminates when it receives a packet matching
    eot_kwd
    '''
    def rx_data(self, data_pipe):
        output_enable = True
        while True:
            rx_d, rx_a = self._sock.recvfrom(self._udp_rx_bufsize)
            if rx_a == self._dest_dev[0]:
                if rx_d == self._eof_kwd:
                    print('eth_rx: recv eof_kwd, terminating')
                    data_pipe.send(False)
                    break
                if rx_d == self._eot_kwd:
                    print('eth_rx: recv eot_kwd, terminating')
                    break
                if output_enable:
                    data_pipe.send(rx_d)
