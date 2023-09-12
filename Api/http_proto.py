from socket import socket
from json import loads



class Response:
	"""
 	מחלקה לתקשורת בפרוטוקול
  	http
   	אין תמיכה בהצפנה
	מטרת המחלקה היא לבצע בדיוק את העבודה עם המידע שחוזר בפרוטוקול 
 	http
  	אבל אם פעולות ספציפיות יותר ושקטות יותר
 	"""
    def __init__(self, response:bytes, method="GET"):
		pass

    def __get_status(self):
		"""
  		מחזיר מהחבילת מידע את קוד התגובה של הפרוטוקול
  		"""
		pass

    def __get_header(self) -> dict:
		"""
  		מחזיר את רשימת הכותרות שחזרו מהשרת
  		"""
		pass

    def __get_json(self) -> dict:
		"""
  		מחזיר את תוכן התגובה כמילון 
  		"""
		pass

    def __get_text(self):
		"""
  		מחזיר את תוכן התגובה כמחרוזת
  		"""
		pass

def payloadHTTP(params: dict) -> str:
	"""
 	מבצע היפוך ממילון לפרמטרים בפרוטוקול 
  	http
 	"""
	pass



def use_http_proto(ip:str, port:int=80, index:bytes=b"/", method:bytes=b"GET", data:dict=None) -> Response:
	"""
 	בונה חבילת מידע ויוצר חיבור לשליחה וקבלה
  	תגובת השרת תחזור בעטיפת המחלקה הנ"ל
 	"""
	pass


