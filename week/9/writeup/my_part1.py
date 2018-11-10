#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashlist = open("../hashes", 'r').readlines()

pw_salts_found = {}

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for line in wordlist:

	if len(pw_salts_found) >= len(hashlist):
		break

	for salt in salts:

		hash_attempt = hashlib.sha512((salt + line.strip()).encode('utf-8')).hexdigest()
		#print (hash_attempt)

		for pw_hash in hashlist:

			pw_hash = pw_hash.strip()

			if hash_attempt == pw_hash:

				pw_salts_found[pw_hash] = [line.strip(), salt]

print (pw_salts_found)
