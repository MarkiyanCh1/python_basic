number_1 = str(input('Enter your first number: '))
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for exponentiation
-> ''')
number_2 = str(input('Enter your second number: '))


if '.' in number_1:
    number_1 = float(number_1)
else:
    number_1 = int(number_1)

if '.' in number_2:
    number_2 = float(number_2)
else:
    number_2 = int(number_2)

print(number_1)
print(number_2)
if operation == '+':
    print(f'Result = {number_1 + number_2}')
elif operation == '-':
    print(f'Result = {number_1 - number_2}')
elif operation == '*':
    print(f'Result = {number_1 * number_2}')
elif operation == '/' and number_2 == 0:
    print("Error - You can't divide on zero")
elif operation == '/':
    print(f'Result = {number_1 / number_2}')
elif operation == '**':
    print(f'Result = {number_1 ** number_2}')
else:
    print("Error - Incorrect sign")
