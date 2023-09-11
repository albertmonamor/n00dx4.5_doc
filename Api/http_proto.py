from socket import socket
from json import loads



class Response:
	
    def __init__(self, response:bytes, method="GET"):
		pass

    def __get_status(self):
		pass

    def __get_header(self) -> dict:
		pass

    def __get_json(self) -> dict:
		pass

    def __get_text(self):
		pass

def payloadHTTP(params: dict) -> str:
	pass

def use_http_proto(ip:str, port:int=80, index:bytes=b"/", method:bytes=b"GET", data:dict=None) -> Response:
	pass


