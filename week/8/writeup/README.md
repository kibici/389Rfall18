Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Kaan Ibici
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kaan Ibici

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. The hackers used the traceroute command on two websites: google.com and csec.umd.edu. This was found by searching for ICMP packets.

2. While searching through TCP packets I found a packet with human-readable text. Following the TCP stream revealed a chat conversation between \nlaz0rh4x and c0uchpot4doz.

3. The packet TCP stream found in (2) contain packets to and from laz0rh4x, whose IP address is 104.248.224.85. By looking at nearby packets \ncommunicating with the same port on Cornerstone Airlines' server from different IP address, I found that c0uchpot4doz's IP address is 206.189.113.189. \nUsing a IP geolocation lookup I found that laz0rh4x is in North Bergen, New Jersey, and c0uchpot4doz is in London.

4. The hackers are communicating over port 2749 on Cornerstone Airlines' server.

5. The hackers mention that "it" will be happening "tomorrow at 1500"

6. The following link was sent in the chat: https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7. The hackers expect to see eachother the following day. 

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*

1. The timestamp for update.fpff is October 24th, 2018 at 10:40pm

2. The author for the fpff file is laz0rh4x

3. The file header indicates that there are 9 sections, but parsing the file reveals 11 sections.

4. Abridged output:

< SECTION 0 >
TYPE: SECTION_ASCII
CONTENT:

Call this number to get your flag: (422) 537 - 7946


< SECTION 1 >

TYPE: SECTION_WORDS
CONTENT:

3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 


< SECTION 2 >

TYPE: SECTION_COORD
CONTENT:

(38.99161, -77.02754)


< SECTION 3 >

TYPE: SECTION_REFERENCE
SECTION REFERENCED: 1

< SECTION 4 >

TYPE: SECTION_ASCII
CONTENT:

The imfamous security pr0s at CMSC389R will never find this!


< SECTION 5 >

TYPE: SECTION_ASCII
CONTENT:

The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}


< SECTION 6 >

TYPE: SECTION_COORD
CONTENT:

(38.9910941, -76.9328019)


< SECTION 7 >

TYPE: SECTION_PNG
png data written to update_sec7.png 

< SECTION 8 >

TYPE: SECTION_ASCII
CONTENT:

AF(saSAdf1AD)Snz**asd1


< SECTION 9 >

TYPE: SECTION_ASCII
CONTENT:

Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9



< SECTION 10 >

TYPE: SECTION_DWORDS
CONTENT:

4 8 15 16 23 42 

5. 
	1. Flag encoded into phone number displayed in section 0: hackerswin
	2. Flag hidden in section 5 text: CMSC389R-{PlaIN_difF_FLAG}
	3. Flag in png file in section 7: CMSC389R-{c0rn3rst0ne_airl1n3s_to_the_m00n}
	4. Flag encoded in base 64 in section 9: CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}

