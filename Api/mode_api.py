import os
from PIL.ImageGrab import grab
import io
from time import sleep
from json import dumps
import shutil as sht
from ctypes import windll
import string
from Api.protocol import OK, BLOCK_FRM, SUM_BLOCKS
from Api.tcp_stream import MainTcpStreamer, read_from_file, write_to_file
from Api.error_api import PACKET_ERROR
from Api.config_packet import SetBlockPacket, GetBlockPacket
from Api.ManaIO import yield_file, open_file, ManaFileFolder, TypeFileBinary, MAX_SIZE_EDITOR, yield_4096_byte_array
from Api.scanner_api import run_shell, scan_by_payload


# ----------------------------------------------
# /* API MODES */
# ----------------------------------------------
# 1. mode shell
# 2. mode screen
# 3. mode explorer
# 4. mode download
# 5. mode upload


def mode_shell(setting_sock, port, parent_setting):
	pass

def mode_screen_tcp(setting_sock, port, parent_setting):
	pass

def mode_screen_tcp_v2(setting_sock, port, parent_setting):
	pass

def ModeExplorer(setting_sock, port, parent_setting):
	pass

def ModeDownload(setting_sock, port, parent_setting=None):
	pass

def ModeUpload(setting_sock, port, parent_setting=None):
	pass

def mode_scanner(setting_sock, port, parent_setting=None):
	pass

def set_X_parts_grab(grb, buffer:io.BytesIO, pkg:list[bytes], xp=3) -> bytes:
	pass

def listdir(path) -> str:
	pass

def list_drives():
	pass

def rename(path, n_path) -> int:
	pass

def del_force(path: str):
	pass

def is_valid_file_to_edit(path) -> int:
	pass


