Writeup 3 - OSINT II, OpSec and RE
======

Name: Kaan Ibici
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kaan Ibici

## Assignment 3 Writeup

### Part 1 (100 pts)

**Poor username/password choice:**
Fred's choice of username and password for his admin server made it extremely easy to access the port that was left open. This is obviously a significant problem since a malicious person with access to the server can steal important information and wreak havoc on the server. Fred's username is the same name as the email he displays on the main page, and is the same name (with the exception of the trailing numbers) he uses for his social media. Not only is Fred's password, "pokemon", simple enough to be found in a list of leaked passwords, but one could easily guess the password by looking at the amount of pokemon content present in his social media posts. Fred could simply use a password that is harder to guess/bruteforce (make it longer, use numbers, special characters, etc), or, in order to ensure that his password is almost impossible to crack, Fred could use a public/private-key pair (RSA) where each device used to access the server has its own private key stored on it. Due to the length of a private-key, it could take millions of years to brute-force, so realisticaly the only way someone would be able to break into the server is by having access to a computer with a private key stored on it.

**Access to admin server IP adress**
Anybody can easily discover the ip address for Fred's admin server just by going to the cornerstone airlines webpage and clicking around. Without the ip address, I would not have been able to do a port scan or nc the server, etc, so it's obvious that it should not be easily discoverable. Additionly having a "admin" link on the front page, and one which directs you to a page with its ip address as the URL, is practically welcoming attempts to find more vulnerabilities.  The simple solution to this would be to not have a link within the website that could direct users to the admin page, and instead just keep the ip address somewhere that is only accessable to trusted users. Anyone who would need to access the admin page would be able to do so by simply typing the ip address into the search bar, and the ip address would not be advertised on the front page.

**Disclosure of personal information**
Social engineering enables malicious people to obatain important information directly from users through deceptive tactics. Effective and inconspicuous social engineering relies on the ability to research a target and find out things such as their interests, habits, behaviors, relationships, etc. Fred's website contains his picture and personal email, which contains the same nick name that he uses for all of his social networks, which are all public. This would allow a social engineer to find out a lot of personal information about Fred (like how big of a pokemon fan he is) without much searching. Fred could reduce his risk of being targeted by social engineering tactics by dissasociating as much personal information from his professional webpage as possible. He could maybe link more professional (public) social network accounts to his webpage if need be, and keep his personal pages private. Additionally, using an email that isn't used for all of his online endeavors (accounts, shopping, etc) would be smart as well.
