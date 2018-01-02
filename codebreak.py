#!/usr/local/bin/python
'''
Project name : codebreak

Overview:
Find out the meaning of the sentence below.

Sentence to crypt: QM YR JYQR WMS YPC Y NWRFML ESW.
Expected answer:   So at last you are a python guy.

Logic is as below:

 A -> C
 B -> D
 C -> E
 D -> F

Alphabet A implies C, Alphabet B implies D, Alphabet C implies E,Alphabet D implies F.

What you will be Using:
string modules, Print, continue, Breaks, list

My Thoughts on Project:
A very fun beginning project, have fun with this... Come up with some great logics! Also, this project really gets you to experiment with strings, functions of strings and also the list operator
'''
import re
c_input = raw_input("Enter your code to decrypt")
c_newword = ""
c_output =""
# split the input string into words by default space delimiter
for c_word in c_input.split():
    #split the words into chars
    for c_latter in c_word:
        #If the char is not an alpha numaric, add char to newstring as it is.
        if re.match(c_latter,'[^\w]'):
            c_newword = c_newword + c_latter
        elif c_latter is 'Z':
            c_newword = c_newword + 'B'
        elif c_latter is 'Y':
            c_newword = c_newword + 'A'
        else:
            # if the char is not Y or Z get the ascii number of char and add 2 to the ascii,get char value of ascii genrated
            #append new char to new word
            c_newword = c_newword + chr(ord(c_latter) + 2)
    c_output = c_output + c_newword + " " # c_input string is split by space so we are adding space at end of each word.
    c_newword = ""
print(c_output.capitalize())
