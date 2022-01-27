#question 1 write a function that takes a string as input and
#returns true if the input string has more vowels than consonants
#returns false if the input string has more consonants than vowels
#returns none if the input string has an equal number of consonants and vowels
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
string = "abc de"
print(totalConsonants(string))