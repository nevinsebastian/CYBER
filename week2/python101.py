#!/bin/python3

print("strings and things:")
print("""hello this is
a muliti line string""")

print ("this is "+"a string")

print('\n') #nev line

#math
print("math time:")
print(50 + 50)#add
print(50 -50)#minus
print(50 *50)#mul
print(50 /  50)#div
print(50 + 50 - 50 * 50 / 50 )#pendas
print(50 ** 2)#expo
print(50 % 6)#modulo
print(50 // 6) #number without leftovers

print('\n') #nev line

#variable & methods

print("fun with variables and methos")
quote = "all is fair in love"
print(len(quote))#length
print(quote.upper())#uppercase
print(quote.lower())# lower
print(quote.title())#title

name ="Nevin"
age = 21
gpa = 9.8
print(int(age))

print("my name is " + name + " and i am " + str(age) + " years old")


print('\n') #nev line

age += 1
print(age) 

birthday = 1
age += birthday
print(age)

print('\n') #nev line

#functions
print(" Now some functions")
def who_am_i():
	name = "Nevin"
	age = 21
	print("my name is " + name + " and i am " + str(age) + " years old")
who_am_i()

#adding in parameters

def add_one_hundred(num):
	print(num + 100)
add_one_hundred(100)

#add in multile parameters
def add(x,y):
	print(x + y)
add(7,7)

#using return
def multiply(x,y):
	return x * y
print(multiply(7,7))

def square_root(x):
	return x ** .5
print(square_root(64))

print('\n') #nev line

#boole expression (true or false)

print("Boolean Expressions:")
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

#relational and boolean operations

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7 > 8 ) and (5 < 7)
test_or = (7 > 5 ) or (5 < 7)
test_not = not True

print(test_and,test_or,test_not)


print('\n') #nev line

#conditional statments
print("Conditional Statments:")
def soda(money):
	if money >= 2:
		return "You`ve got a soda"
	else:
		return "No soda for u!"
print(soda(3))
print(soda(1))

print('\n') #nev line


def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "we are getting JAVAN"
	elif (age >= 21) and (money < 5):
		return "come back with more money"
	elif (age < 21) and (money >= 5):
		return "nice try kidd"
	else:
		return "you are too poor and too yound"
	
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))


print('\n') #nev line

#Lists 

print("List have brackets:")
movies = ["churuli","RDX","kok"]

print(movies[0])
print(movies[0:3])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("kurup")
print(movies)

movies.pop()
print(movies)

movies.pop(1)
print(movies)

movies = ["churuli","RDX","kok"]
person = ["karataikid","wolfofwall"]

combined = zip(movies, person)
print(list(combined))


#Tuples
print("Tuples have parentheses and cannot change")
grades = ("A","B","C","D","E","F")
print(grades[1])

# Looping
print("for loops - start to finsh of iterate:")
vegitables = ["cucumber","spinach","cabbage"]
for x in vegitables:
	print(x)
	
print("while loop- execute as long as true:")
i = 1
while i <= 10:
	print(i)
	i +=1
	

