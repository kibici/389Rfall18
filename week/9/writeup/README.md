Writeup 9 - Crypto I
=====

Name: Kaan Ibici
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kaan Ibici

## Assignment 9 Writeup

### Part 1 (60 Pts)

Since we know the hash (sha512) and salt type (prepended lowercase character) used for the list of hashes, a simple brute force method can find the corresponding password and salt for each password hash in linear time, assuming the passwords exist in the chosen password dump. My script takes each plaintext password and tries salting and hashing once for each possible salt, and then compares it with each password hash to see if a successful password-salt pair has been found, in which case the pair is stored in a dictionary with the corresponding hash as the key. The program terminates after all hashes in the list have password-salt pairs, or once the password list is exhausted. 

Solution found: 

'c35eb97205dd1c1a251ad9ea824c384e5d0668899ce7fbf269f99f6457bd06055440fba178593b1f9d4bfbc7e968d48709bc03e7ff57056230a79bc6b85d92c8': ['jordan', 'm'], 'd39d933d91c3e4455beb4add6de0a48dafcf9cb7acd23e3c066542161dcc8a719cbac9ae1eb7c9e71a7530400795f574bd55df17a2d496089cd70f8ae34bf267': ['loveyou', 'u'], '9a23df618219099dae46ccb917fbc42ddf1bcf80583ec980d95eaab4ebee49c7a6e1bac13882cf5dd8d3850c137fdff378e53810e98f7e9508ca8516e883458e': ['neptune', 'k'], '70a2fc11b142c8974c10a8935b218186e9ecdad4d1c4f28ec2e91553bd60cfff2cc9b5be07e206a2dae3906b75c83062e1afe28ebe0748a214307bcb03ad116f': ['pizza', 'p']

[Script for part 1](my_part1.py)
[Screenshot of output](my_part1_sc.png)

### Part 2 (40 Pts)

I played around with the hash workshop very breifly to get an understanding of the messages sent by the server. I concluded that every question had the same format: "Find me the {hash type} hash of {plaintext}". I wasn't quite sure what other message formats I'd encounter, or where this prompt would be located in the entire message; I decided to search each message for the word "Find" and take the 3rd word after as the hash type and the 6th word after as the plaintext to hash (didn't have time to familiarize myself with regex in python), or quit the program if "Find" isn't found. I have a case for each hash type in hashlib that is checked against the found hash type, and when the matching case is found the hash is computed and sent to the socket with a new line to submit the answer.

Solution found:

CMSC389R-{H4sh-5l!ngInG-h@sH3r}

[Script for part 2](my_part2.py)
[Screenshot of output](my_part2_sc.png)
