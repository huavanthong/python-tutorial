############ Lesson 1: ################
# Before we have decorator pattern,
# we can assign function equal another function
########################################
# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
	return text.upper() 

print(shout('Hello')) 

yell = shout 

print(yell('Hello')) 

############ Lesson 2: ################
# Before we have decorator pattern, 
# we can assign a function to another function
########################################
# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
	return text.upper() 

def whisper(text): 
	return text.lower() 

def greet(func): 
	# storing the function in a variable 
	greeting = func("""Hi, I am created by a function passed as an argument.""") 
	print (greeting) 

greet(shout) 
greet(whisper) 
