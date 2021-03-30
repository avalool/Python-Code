employees = ["Olivia", "Amanda", "Tabitha"]
"olivia" in employees

#.lower

employees = ["olivia", "amanda", "tabitha"]
"Olivia".lower()
'olivia'

"olivIa".lower()
'olivia'

"Olivia".lower() in employees
True


#.upper

"Tabitha".upper()
'TABITHA'

#.title

"world health organisation".title()
'World Health Organisation'

#.replace

"All is well".replace("is", "eez")
'All eez well'

#.split

"All is well".split()
['All','is', 'well']

"1+2+3+4+5+6+7+8".split("+")
['1', '2', '3', '4', '5', '6', '7', '8']

new_list = "1+2+3+4+5+6+7+8".split("+")

new_list
['1', '2', '3', '4', '5', '6', '7', '8']

"+".join(new_list)
'1+2+3+4+5+6+7+8'

#.strip

strng = "All is well".center(15)

strng
'    All is well    '

strng.strip()
'All is well'

#.translate

"This is a test".translate("is", "ez")