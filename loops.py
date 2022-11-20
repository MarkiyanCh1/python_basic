# # 1
# counter = 0
# element = " "
# row_numbers = 3
# vowels = "AaEeIiOoUuYy"
# while counter < 1:
#     string = input('Enter any string: ')
#     check_for_numbers = [number.isdigit() for number in string]
#     number = 0
#     for flag in check_for_numbers:
#         if flag:
#             number += 1
#         else:
#             number = 0
#         if number == row_numbers:
#             print("3 digits in a row were entered. The loop is interrupted")
#             counter += 1
#             break
#     else:
#         upper = (''.join(letter for letter in string if letter.isupper()))
#         print('Uppercase characters:', upper)
#         print(f"Index of spaces: {[space for space, character in enumerate(string) if character == element]}")
#         vowel = [vow for vow in string if vow in vowels]
#         print(f"Vowel letters: {vowel}")
#         print("The loop has been completed successfully")
#         counter += 1

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
