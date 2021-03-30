"""String Methods
.strip() #removes spaces at the ends of the string
.split() #changes on string into a list of strings
.join() #puts together a list of strings into one string
.center() #centralizes a string by adding spaces at the sides
.replace() #exchanges one type of word with another in a string
.lower() #changes all letters in the string to lowercase
.upper() #puts all letters in uppercase
.find() #searches for a sub-string (word) in the given string. Returns -1 if not found
.title() #capitalizes the first letter of each word in a string"""

# write a program that creates an acronym of the sentences given to it

sentence = "united states of america"
# desired result USA
words = sentence.split()
print(words)
acronym = ""
for word in words:
    acronym = acronym + word[0]
"""print(word[0]) #indexing"""
print(acronym.upper())