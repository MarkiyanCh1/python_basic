# 1
counter = 0
element = " "
row_numbers = 3
vowels = "AaEeIiOoUuYy"
while counter < 1:
    string = input('Enter any string: ')
    check_for_numbers = [number.isdigit() for number in string]
    number = 0
    for flag in check_for_numbers:
        if flag:
            number += 1
        else:
            number = 0
        if number == row_numbers:
            print("3 digits in a row were entered. The loop is interrupted")
            counter += 1
            break
    else:
        upper = (''.join(letter for letter in string if letter.isupper()))
        print('Uppercase characters:', upper)
        print(f"Index of spaces: {[space for space, character in enumerate(string) if character == element]}")
        vowel = [vow for vow in string if vow in vowels]
        print(f"Vowel letters: {vowel}")
        print("The loop has been completed successfully")
        counter += 1

# 2
while True:
    first_data = str(input(f"Enter the first operand: "))
    second_data = str(input(f"Enter the second operand: "))
    operation = str(input(f"Enter an operation/Enter exit to complete: "))
    if operation == "exit":
        print("The process is completed")
        break
    if '.' in first_data:
        operand_one = float(first_data)
    else:
        operand_one = int(first_data)

    if '.' in second_data:
        operand_two = float(second_data)
    else:
        operand_two = int(second_data)

    if operation == '+':
        print(f'Result = {operand_one + operand_two}')

    elif operation == '-':
        print(f'Result = {operand_one - operand_two}')

    elif operation == '/' and operand_two == 0:
        print("You can't divide on zero")

    elif operation == '/':
        print(f'Result = {operand_one / operand_two}')

    elif operation == '*':
        print(f'Result = {operand_one * operand_two}')

    elif operation == '**':
        print(f'Result = {operand_one ** operand_two}')
    else:
        print(f"Invalid operation between numbers ")
