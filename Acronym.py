sentence = "visual studio Code"
# desired result is VSC
words = sentence.split()
acronym = ""
for word in words:
    acronym = acronym + word[0]
print(acronym.upper())