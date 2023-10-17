#!/bin/python3

#Importing
print("Importing is important")


import sys #system functions and parameters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #importing with an alias
print(dt.now())

def new_line():
	print('\n')
	
new_line()

#Advanced Strings
print("Advanced strings:")
my_name = "Nevin"
print(my_name[0])
print(my_name[-1])

sentence = "this is a sentence"
print(sentence[:4]) # to print the first word
print(sentence[-9:-1])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))



qouteception = "I sed, 'give me all the money"
print(qouteception)

qouteception = "I sed, \"give me all the money\""
print(qouteception)

print("A" in "Apple")
letter = "a"
word= "Apple"
print(letter.lower() in word.lower())# Improved case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

