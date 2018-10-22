Writeup 7 - Forensics I
======

Name: Kaan Ibici
Section: 0201 

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kaan Ibici

## Assignment 7 writeup

### Part 1 (40 pts)

1. The file is a JPEG. This was found using the file command

2. The picture was taken at the 360 CHICAGO building in Chicago, Illinois. This was found by obtaining the gps coordinates with the exiftool command

3. The time stamp for the picture is 2018:08:22 11:33:24 (this was under Original Date/Time, GPS Timestamp is 2018:08:22 16:33:24Z)

4. The photo was taken with an iPhone 8 back camera.

5. The photo was taken at an altitude of 539.5 m above sea level

6. I found one flag by calling the strings command on the image file and using grep: CMSC389R-{look_I_f0und_a_str1ng}. as far as I know there's supposed
to be a second, but using everything in the slides up until steg only got me this one. I have a feeling I should have found it using binwalk, but when I
extracted the files I was not able to uncompress the zlib file. Other than that I'm not sure what I was supposed to do to find it.

### Part 2 (55 pts)

I first used the file command to find the file type of binary, which identified the file as an ELF executable. I then used readelf to get any information
on the file, such as headers/symbols that might indicate the purpose of the executable. Something that caught my attention was the use of the functions 
fopen and fwrite; this indicates that the file creates a file and writes to it. Upon looking at the output of the strings command I saw the characters
"FIFJ", which is JFIF, the common magic bytes for a jpeg, backwards. Since I also saw a array reverse function in the readelf output, I concluded that
the program outputs a jpeg file (I may have also recieved a hint...). I decided to run the executable, which created an output file in my tmp directory.
A file command on the output file, however, concluded that it was a "data" file. I opened the file in a hex editor and found that the magic bytes matched
those of a jpeg, except with two preceding 0 bytes. After removing the bytes, calling file on the output file concluded it was a jpeg file. I figured the 
flag was hidden in the jpeg using steghide, so I used steghide extraction. The passphrase I used was stegosaurus, since I may have overheard that the 
passphrase was the subject of the jpeg itself in office hours. This revealed the hidden flag, CMSC389R-{dropping_files_is_fun}. Many issues were 
encountered in this process. For example, I didn't know to run chmod on a file when it won't run initially, and using vim to remove the problematic bytes
in the jpeg file ended up adding extra bytes that steghide did not like. 