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
string = "random word"
print(totalConsonants(string))

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

print(totalConsonants == findVowelCount)