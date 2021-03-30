"""program that prints out a health warning message 
if one of the patient temperatures is higher than 40 degrees Celsius"""
#Temperatures: 36, 32, 45, 38

temperatures = ['36', '32', '45', '38']
for temperature in temperatures:
    if temperature == '45':
        print('Warning, possible COVID patient! Isolate immediately.')
    else:
        print('No infected patients')