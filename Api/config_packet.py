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
	pass

def XOR(value:str, key:str):
	pass

def _unpad(d):
	pass

def _pad(d: bytes, block: int = AES.block_size, EndBlock: bytes = None):
	pass

def AES_encode(key: bytes, intVector: bytes, data: bytes):
	pass

def AES_decode(key: bytes, intVector: bytes, data: bytes):
	pass

class TCPConfigPacket:
    pass
  
	
def KPacket(inf: bytes, byt: bytes) -> bytes:
	pass

def GetBlockPacket(Packet:bytes, enc=1, key=None, intVector=None, ignore_err=True, loads_binary=False):
	pass

def SetBlockPacket(info: dict, key=None, iv=None, _binary: bytes = b"empty", dump_binary=False) -> bytes:
	pass



