#ask user the price
price = int(input("Please enter the price of your meal: "))
Percentage = input('How much tip would you like to leave? (normal, kind, generous): ')

#calculate % of their meal price
tip=0
if Percentage == 'normal':
    tip = price * 0.18

elif Percentage =='kind':
    tip = price * 0.2

elif Percentage == 'generous':
    tip = price * 0.25

Final = price + tip

print("The final price will be" , Final,'.')
