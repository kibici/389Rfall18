Writeup 3 - Pentesting I
======

Name: Kaan Ibici
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kaan Ibici

## Assignment 4 Writeup

### Part 1 (45 pts)

The though process behind figuring out how to inject commands into the victim server was pretty simple: I new that the up-time system is probably just taking the ip address it's given and then using it in a ping command, so I tried terminating the command with a semi-colon (after finding out that the ip address is the last argument of a ping command) and then followed it with an ls command to see if it worked. As I had hoped, a list of directories was printed, so it was clear that I could search for the flag by formatting the commands I intended to use into one line, beginning with a semi-colon, and then entering the line into the input field of the up-link system. The line I used to search for the flag's location is "; cd home; ls", and the line I used to obtain the flag is "; cat /home/flag.txt". The flag I found was CMSC389R-{p1ng_as_a_$erv1c3}. Fred could have prevented this by sanitizing his input, which would not be hard to do since the essential character in injecting commands, a semi-colon, is not necessary for an ip address. Without a semi-colon a user would not be able to terminate the ping command or add another command afterwars. Hence, simply disallowing any inputs with characters other than numbers and periods would successfully prevent command line injection. He could easily do by iterating through each character of the string and terminating when an invalid character is found, or in bash (which is what Fred uses) it would probably be easier to grep for a semi-colon. I really could not think of much more to talk about to reach 300 words, sorry.

### Part 2 (55 pts)


Program functions: 

	pull <remote-path> <local-path>: 

	My implementation of the pull command allows a user to take files (I'm pretty sure it will only work with ascii files) from the victim server. I did not implement it to allow a user to pull an entire directory. This is done by opening a socket to the victim server and injecting a cat command with the given remote-path, and then writing the output to a file specified by the local-path. If an empty output is returned from the cat call, this means the specified file or path does not exist, or that the file is empty, and an error is printed. The command to open the local fileis enclosed in a try-except block which prints an error if there was an issue in opening the file. 


	shell: 

	The shell function essentually creates a remote shell by constantly opening new socket connections to the up-time system and injecting commands one at a time, while appearing to operate on a constant connection to the user. This is necessary because only one line can be injected into the up-time system at a time. The remote shell keeps track of the current directory, which it displays on the command line. Before sending each command to the up-time system, a cd command with the current path is placed before it so that, while each new connection starts in the root directory, the user's command is executed in the intended directory. When a user inputs a cd command, a pwd command is added to the end of it so that the current directory can be updated. The current implementation does not work if a user inputs multiple commands containing at least one cd command, in a single line, so the function only allows one input at a time since fixing this would be tedious.


	help:

	Prints a menu describing function. The same menu is displayed if an invalid input is given. 


	quit:

	quits the shell







