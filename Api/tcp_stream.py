from socket import *

from Api.error_api import PACKET_ERROR
from Api.protocol import OK


class MainTcpStreamer(socket):
	
    def __init__(self, ip, port=None, *a, **kw):

		pass

    def open_socket(self) -> bool:
		"""
  		יצירה של שקע כולל התחברות
  		"""
		pass

    def get_packet(self, buf_size=1024) -> bytes | int:
		"""
  		קבלת מידע ע"פ הפרוטוקול
  		"""
		pass

    def send_packet(self, packet) -> None | int:
		"""
  		שליחת מידע ע"פ הפרוטוקול
  		"""
		pass

    def communication(self, packet):
		"""
  		מפעיך את
		get_packet & send_packet
  		ביחד
  		"""
		pass



def receive_proto(sock:socket, buff_size=1024) -> bytes:
	"""
 	קבלת מידע ע"פ הפרוטוקול
 	"""
	pass

def send_proto(sock:socket, packet:bytes) -> int:
	"""
 	שליחת מידע ע"פ הפרוטוקול
 	"""
	pass

def read_from_file(h_file, sock:socket):
	"""
 	קריאה מקובץ בקצב של 4096
 	"""
	pass

def write_to_file(h_file, sock:socket, size_file):
	"""
 	כתיבה לקובת בקצב של 4096
 	"""
	pass
