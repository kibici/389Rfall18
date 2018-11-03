#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

################
# PARSE HEADER #
################

offset = 0
data_to_parse = 24
magic, ver, time, auth, num_secs = struct.unpack("<LLLQL", data[offset:(offset+data_to_parse)])
offset = offset + data_to_parse

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if ver != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(ver), int(VERSION)))


print("\n------- HEADER -------\n")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(ver))
print("TIMESTAMP: %s" % datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S'))
print("AUTHOR: %s" % format(auth, 'x').decode('hex')[::-1])
print("SECTION COUNT: %d" % int(num_secs))

##############
# PARSE BODY #
##############

print("\n-------  BODY  -------\n")

sec_num = 0

while offset < len(data):

	data_to_parse = 8
	stype, slen = struct.unpack("<LL", data[offset:(offset+data_to_parse)])
	offset = offset + data_to_parse
	
	#PNG

	data_to_parse = int(slen)
	sec_data = data[offset:(offset+data_to_parse)]
	offset = offset + data_to_parse

	print("\n< SECTION %d >\n" % sec_num)

	if int(stype) == 1:

		png_data = "\211PNG\r\n\032\n" + sec_data

		fname = sys.argv[1].split('.')[0] + "_sec" + str(sec_num) + ".png"
		f = open(fname, "w")
		f.write(png_data)

		print("TYPE: SECTION_PNG")
		print("LENGTH: %d" % int(slen))
		print("png data written to " + fname)

	#DWORDS

	elif int(stype) == 2:

		ind = 0
		content = "\n"
		while(ind < len(sec_data)):
			content = content + str(struct.unpack("<Q", sec_data[ind:(ind+8)])[0]) + " "
			ind = ind + 8

		print("TYPE: SECTION_DWORDS")
		print("LENGTH: %d" % int(slen))
		print("CONTENT:\n" + content + "\n")

	#UTF8

	elif int(stype) == 3:
		
		print("TYPE: SECTION_UTF8")
		print("LENGTH: %d" % int(slen))
		print("CONTENT:\n\n" + sec_data.decode('utf-8') + "\n")

	#DOUBLES

	elif int(stype) == 4:

		ind = 0
		content = "\n"
		while(ind < len(sec_data)):
			content = content + str(struct.unpack("<d", sec_data[ind:(ind+8)])[0]) + " "
			ind = ind + 8

		print("TYPE: SECTION_DOUBLES")
		print("LENGTH: %d" % int(slen))
		print("CONTENT:\n" + content + "\n")

	#WORDS 

	elif int(stype) == 5:

		ind = 0
		content = "\n"
		while(ind < len(sec_data)):
			content = content + str(struct.unpack("<L", sec_data[ind:(ind+4)])[0]) + " "
			ind = ind + 4

		print("TYPE: SECTION_WORDS")
		print("LENGTH: %d" % int(slen))
		print("CONTENT:\n" + content + "\n")

	#COORD

	elif int(stype) == 6:

		coord_lat, coord_long = struct.unpack("<dd", sec_data)
		print("TYPE: SECTION_COORD")
		print("LENGTH: %d" % int(slen))
		print("CONTENT:\n\n" + str((coord_lat,coord_long)) + "\n")

	#REFERENCE 

	elif int(stype) == 7:

		sec_ref = struct.unpack("<l", sec_data)
		print("TYPE: SECTION_REFERENCE")
		print("LENGTH: %d" % int(slen))
		print("SECTION REFERENCED: %d" % int(sec_ref[0]))

	#ASCII

	elif int(stype) == 9:

		print("TYPE: SECTION_ASCII")
		print("LENGTH: %d" % int(slen))
		print("CONTENT:\n\n" + sec_data + "\n")

	else:
		bork("Invalid section format")

	sec_num = sec_num + 1



