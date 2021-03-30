# program to simulate a calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input('Operation(add, subtract, divide, floor divide, multiply): ')

if operation == "add":
    result = num1 +num2

elif operation == "subtract":
    result = num1 - num2

elif operation == 'divide':
    result = num1 / num2

elif operation == 'floor divide':
    result = num1 // num2

elif operation == 'multiply':
    result = num1 * num2
    
print(result) 