Writeup 5 - Binaries I
======

Name: Kaan Ibici
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kaan Ibici

## Assignment 5 Writeup

I started thinking about how to implement memset in x86 assembly by first writing out the step by step operations the program needed to complete in order to mimick the C code for memset, in somewhat of a pseudo-assembly code. I knew my program needed a loop, and therefore I needed a register to hold a counter, and I needed to zero the counter before the loop by xor-ing the counter with itself. I didn't use the loop instruction for my loop, since I wanted to have an ascending counter that starts from 0 so that I can use it to offset the pointer to the string I'm modifying, so instead I used a cmp instruction with the counter and the given string length as arguments. If the cmp instruction resulted in a zero, this means the counter = the string length and the loop should finish, so I follow the cmp instruction with a jz instruction that jumps to my return. After checking if the loop is finished, I need to set the ith character of the string to the given character with a mov instruction where the address of the string is offset by the counter. After setting the character I increment the counter and then jmp back to the loop. After planning out the program, I figured out the appropriate registers to use for each argument and the counter by refering to the lecture slides to use and then typed it out. The inplementation for the strncpy function was almost exactly the same, except instead of replacing each character in the given string with a single character, I set each character to the corresponding character at the same index in a diffent string. Since the mov instruction doesn't allow memory to memory transactions, I had to first store the character from the second string in a new register, and then use a mov instruction to move the character from the register to the desired index in the first string. other than that, the program is exactly the same. To my delight, the only issues I encountered in running my programs were a few syntax errors, and realizing I needed Kali Linux to compile them (I did not have Kali). My programs worked as desired upon my first compilation! Wow!

