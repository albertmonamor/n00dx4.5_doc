import os, winreg
from random import randint
from Api.protocol import  NOOD_NAME,  startup_keys


TypeFileBinary = []   # // real value not here
MAX_SIZE_EDITOR = 0  # // real value not here


class ManaFileFolder:
	
    def __init__(self, path: str, save_as: str = None):
		pass

    def CreatePath(self) -> str:
		pass

    def isHidden(self, path=None) -> bool:
		pass

    def SaveAs(self):
		pass

    def GetBase(self):
		pass

def yield_file(file: 'open_file', path) -> bytes | str:
	pass

def open_file(path, Mode="rb") :
	pass

def yield_4096_byte_array(_byte):
	pass

def set_trojan_start_on_up(path_trojan:str) -> bool:
	pass

def verify_key_is_exist(with_this_path:str, key_win_object:winreg.OpenKey=None, name_key=None) -> tuple[bool, bool]:
	pass

def delete_key(name:str) -> int:
	pass

def CLEANUP():
	pass

