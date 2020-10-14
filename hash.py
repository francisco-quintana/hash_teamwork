import hashlib

def hashear(message):
	salt = b'<6dMX.ry'
	message = message.encode()
	hash_ = hashlib.pbkdf2_hmac('sha256', message, salt, 100000)
	hs=hash_.hex()
	return hs