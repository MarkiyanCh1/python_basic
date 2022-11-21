# 1
user_string = input('Enter any string: ')
upper = ''
vowels = ''
number_of_digits = 0

for element in user_string:
    if element.isdigit():
        number_of_digits += 1
        if number_of_digits == 3:
            print("The loop is interrupted")
            break
    else:
        if element.isupper():
            upper += element
        if element in "AaEeIiOoUuYy":
            vowels += element
        indexes_of_spaces = [index for index, space in enumerate(user_string) if space in ' ']

print('Uppercase characters:', ', '.join(upper))
print(f"Index of spaces: {indexes_of_spaces}")
print(f"Vowel letters: {vowels}")

# 2
while True:

    number_1 = str(input(f"Enter the first operand/Enter exit to complete: "))
    if number_1 == "exit":
        print("The process is completed")
        break
    number_2 = str(input(f"Enter the second operand/Enter exit to complete: : "))
    if number_2 == "exit":
        print("The process is completed")
        break

    operation = str(input(f"Enter an operation/Enter exit to complete: "))
    if operation == "exit":
        print("The process is completed")
        break

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
        print(f'Result {number_1} {operation} {number_2} = {number_1 + number_2}')
    elif operation == '-':
        print(f'Result {number_1} {operation} {number_2} = {number_1 - number_2}')
    elif operation == '*':
        print(f'Result {number_1} {operation} {number_2} = {number_1 * number_2}')
    elif operation == '/' and number_2 == 0:
        print("Error - You can't divide on zero")
    elif operation == '/':
        print(f'Result {number_1} {operation} {number_2} = {number_1 / number_2}')
    elif operation == '**':
        print(f'Result {number_1} {operation} {number_2} = {number_1 ** number_2}')
    else:
        print("Error - Incorrect sign")
