#question 1 write a function that takes a string as input and
#returns true if the input string has more vowels than consonants
#returns false if the input string has more consonants than vowels
#returns none if the input string has an equal number of consonants and vowels
from filecmp import cmp


def findNumConsonant(ch): #method for seeing how many consonants found on geeksforgeeks
	ch = ch.upper() #to deal with uppercase letters first
#telling to not return any of the uppercase vowels
	return not (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' and ord(ch) >= 65 and ord(ch) <= 90)

def totalConsonants(string): #now we're going to be counting the consonant amount
	count = 0
	for i in range(len(string)):
		#checking if the character is a consonant
		if (findNumConsonant(string[i])):
			count += 1
	return count

#driver code
string = "random word"
print("Number of consonants: ", totalConsonants(string))

#now to find the amount of vowels
def findVowelCount(str): #method to find how many vowels. code taken from geeksforgeeks
    count = 0 #initialize 
    vowel = set("aeiouAEIOU") #creating set of vowels

    for alphabet in str: #loop to go through the entire alphabet in the string
            if alphabet in vowel:
                count = count + 1

    print("Number of vowels: ", count)

str = "random word"
findVowelCount(str)

#a = totalConsonants
#b = findVowelCount
#cmp(a,b) 

#question 7 write a function that takes a list of integers and returns the same list without any duplicates
mylist = ["3", "7", "7", "1", "1"] #set up the list #method found on code grepper
mylist = sorted(set(mylist))        #sorting the list then printing it
print(mylist)

#question 2
import math #using codespeedy to check if the method is right
r=float(input("Enter cylinder radius: "))
h=float(input("Enter cylinder height: "))
surfaceArea=2*math.pi+pow(r,2)*h
volume = math.pi*pow(r,2)*h

print("Surface area of cylinder will be %.2f" %surfaceArea)
print("Volume of a cylinder will be %.2f" %volume)

#question 3 write a function that takes a list of strings as inputs and then returns a single string created by joining all the input strings together
print(",".join(["pls", "read", "stormlight", "archives", "if", "you", "read"])) #using digitalocean to figure out .join method

#question 8 create a new folder in current directory
#method from codegrepper
import os
os.mkdir('hw3-folder')

#question 6 use try/except statements and catch ZeroDivisionError
#zetcode used
def nums():
	a = float(input("First number: "))
	b = float(input("second number: "))
	return a, b

x, y = nums()

try:
		print(f"{x} / {y} os {x/y}")

		except ZeroDivisionError:
				print("Can't divide by zero")
                x, y = input_numbers()