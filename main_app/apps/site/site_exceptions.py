from fastapi import HTTPException, status


class SomeException(HTTPException):
	def __init__(self):
		self.status_code = 400
		self.detail = "some error msg"
