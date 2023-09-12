import subprocess as sub
import os, re
from time import sleep
from json import dumps, loads

from Api.ManaIO import set_trojan_start_on_up, CLEANUP
from Api.protocol import NOOD_NAME, NOOD_PATH, H_T_NAME


KEY_S = ''
KEY_XOR = ''
ALG = ''

def new_key_xor():
	"""
 	ערך חדש למפתח ההצפנה 
  	KEY_XOR
 	"""
	pass

def XOR(value:str, key:str):
	"""
 	פעולה הופכית לכל תו ותו, להצפנה הקלאסית
 	"""
	pass

def _unpad(d):
	"""	
	כחלק מפרוטוקול
 	AES
 	d[:-len(d)] = d[-1] = ord(d[-1]) = length of bytes that append to complete block_size
 	"""
	pass

def _pad(d: bytes, block: int = AES.block_size, EndBlock: bytes = None):
	"""
	    הסבר קצר  
	    16 is AES.block_size
	
	    if d {data} length == 16 bytes need 16 bytes more
	    if d lower of 16 bytes, need complete data to 16 bytes
	    if d length = 16, so! >
	    16-(16%16) == 16 { module return integer 16%16 -> 0 -> -16 %16 -> 16 integer}
	    so!! d +(16 - len(d) % 16) * chr(16 - len(d) % 16) = d + (16*chr(16))
	    example:
	        ord("\x016") = chr(16) = 16 = length of bytes that append
	        chr(12) = ord("\x012") = 12 = length of bytes that append
	
	    סיכום
	    just <16.
	    16> not exist
	    because need block_size up to 16
 	"""
	pass

def AES_encode(key: bytes, intVector: bytes, data: bytes):
	"""
 	צימצום קוד 
 	"""
	pass

def AES_decode(key: bytes, intVector: bytes, data: bytes):
	"""
 	צימצום קוד
 	"""
	pass

class TCPConfigPacket:
	"""
 	מחלקה בוטלה
 	"""
    pass
  
	
def KPacket(inf: bytes, byt: bytes) -> bytes:
	"""
 	חלק מהפרוטוקול, משרשר וחותם את חבילת מידע לפני שליחה לצד השני
 	"""
	pass

def GetBlockPacket(Packet:bytes, enc=1, key=None, intVector=None, ignore_err=True, loads_binary=False):
	"""
	כחלק מהפרוטוקול, מפרק את חבילת המידע אחרי שהתקבל דרך החיבור
 	
    :param loads_binary: Nbone
    :param Packet: recv(1024 up tp 4096)
    :param key: 32 length
    :param intVector: 16 length
    :param enc:  0 return just body packet 1 all
    :param ignore_err: crash or return PACKET_ERROR
    :return:
    """
	pass

def SetBlockPacket(info: dict, key=None, iv=None, _binary: bytes = b"empty", dump_binary=False) -> bytes:
	"""
 	בונה חבילת מידע על פי הפרוטוקול, 
  	:param info: dict
    :param _binary: bytes
    :param key: length of 32 for AES
    :param iv: length of 16 for vector AES
    :param dump_binary: json.dumps(_binary) binary from type() dict
    :return: packet
 	"""
	pass



