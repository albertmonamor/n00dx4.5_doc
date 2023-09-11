from socket import *

from Api.error_api import PACKET_ERROR
from Api.protocol import OK


class MainTcpStreamer(socket):
	
    def __init__(self, ip, port=None, *a, **kw):
		pass

    def open_socket(self) -> bool:
		pass

    def get_packet(self, buf_size=1024) -> bytes | int:
		pass

    def send_packet(self, packet) -> None | int:
		pass

    def communication(self, packet):
		pass



def receive_proto(sock:socket, buff_size=1024) -> bytes:
	pass

def send_proto(sock:socket, packet:bytes) -> int:
	pass

def read_from_file(h_file, sock:socket):
	pass

def write_to_file(h_file, sock:socket, size_file):
	pass
