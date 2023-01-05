#!/usr/bin/env python

import os
import sys
from base64 import b64encode, b64decode
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from dotenv import load_dotenv

load_dotenv()
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY")

def formatKey(key):
	shrot_key = SHA256.new(key.encode('utf-8')).digest()
	new_key = shrot_key[:16]
	return new_key

def encrypt(key, message):
	cipher = AES.new(key, AES.MODE_ECB)
	message = pad(message.encode('utf-8'), AES.block_size)
	encrypted = cipher.encrypt(message)
	print(b64encode(encrypted).decode('utf-8'))
	return b64encode(encrypted)

def decrypt(key, encrypted):
	encrypted = b64decode(encrypted)
	cipher = AES.new(key, AES.MODE_ECB)
	message = cipher.decrypt(encrypted)
	print(message.decode('utf-8'))
	return message

if __name__ == '__main__':
	mode = sys.argv[1]
	data = sys.argv[2]
	key = formatKey(ENCRYPTION_KEY)
	if mode == 'e':
		encrypted = encrypt(key, data)
	elif mode == 'd':
		message = decrypt(key, data)