#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib


host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
while True:

	data = s.recv(1024)
	msg = data.decode('utf-8')
	print(msg, end="")

	words = msg.split()

	inputs_found = False

	for i in range(len(words)):
		if words[i] == "Find":
			hash_type = words[i + 3]
			to_hash = words[i + 6].strip().encode('utf-8')
			inputs_found = True
			break 
	
	if not inputs_found:
		quit()

	if hash_type == "sha1":
		hashed = hashlib.sha1(to_hash).hexdigest()

	elif hash_type == "sha224":
		hashed = hashlib.sha224(to_hash).hexdigest()

	elif hash_type == "sha256":
		hashed = hashlib.sha256(to_hash).hexdigest()

	elif hash_type == "sha384":
		hashed = hashlib.sha384(to_hash).hexdigest()

	elif hash_type == "sha512":
		hashed = hashlib.sha512(to_hash).hexdigest()

	elif hash_type == "blake2b":
		hashed = hashlib.blake2b(to_hash).hexdigest()

	elif hash_type == "blake2s":
		hashed = hashlib.blake2s(to_hash).hexdigest()
	
	elif hash_type == "md5":
		hashed = hashlib.md5(to_hash).hexdigest()

	print(hashed)
	s.send((hashed + "\n").encode())


# close the connection
s.close()
