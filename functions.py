# Task 1. Sum of numbers in a specified range
start = int(input('Please enter first number  -> '))
end = int(input('Please enter second number -> '))


def sum_in_range(start, end):
    if start > end:
        new_start = end
        end = start
        values = sum(range(new_start, end + 1))
    else:
        values = sum(range(start, end + 1))
    return values


print(f'Task 1-Sum of numbers in a specified range -> {sum_in_range(start, end)}')

# Task 2. Number of seconds to 'dd:hh:mm:ss' format
seconds = int(input('Please enter number of seconds  -> '))


def seconds_to_days(seconds):
    result = []
    time_intervals = [
        ['Years', 60 * 60 * 24 * 7 * 4 * 12],  # 31,104,000
        ['Months', 60 * 60 * 24 * 30],  # 2,592,000
        ['Weeks', 60 * 60 * 24 * 7],  # 604,800
        ['Days', 60 * 60 * 24],  # 86400
        ['Hours', 60 * 60],  # 3600
        ['Minutes', 60],
        ['Seconds', 1],
    ]
    for name, count in time_intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append(f"{value} {name}")
    return ", ".join(result)


print(f'Task 2-Number of seconds to Years, Months, Weeks, Days, Hours, Minutes, Seconds  -> {seconds_to_days(seconds)}')


# Task 3.1. A sum function using the 'for' loop
numbers_for_loop = [21, 5, 11, "55", 3, "10"]


def for_loop_sum(numbers_for_loop):
    counter = 0
    for num in numbers_for_loop:
        if isinstance(num, int):
            counter += num
        elif isinstance(num, str):
            num = int(num)
            counter += num
    return counter


print(f'Task 3.1-A sum function using the FOR loop  -> {for_loop_sum(numbers_for_loop)}')

# Task 3.2. A sum function using the 'while' loop
numbers_while_loop = list(range(1, 15))


def while_loop_sum(numbers_while_loop):
    result = 0
    while numbers_while_loop:
        result = sum(numbers_while_loop)
        break
    return result


print(f'Task 3.2-A sum function using the WHILE loop  -> {while_loop_sum(numbers_while_loop)}')


# Task 3.3. A recursive function
values = [21, 5, 11, 55, 3, 10]


def recursive_sum(values: list):
    if len(values) == 0:
        return 0
    else:
        return values[0] + recursive_sum(values[1:])


print(f'Task 3.3-A sum function using the RECURSION loop  -> {recursive_sum(values)}')

# Task 4. The Fibonacci function


def fibonacci_numbers(number):
    if number <= 0:
        print("Please enter only positive integers")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci_numbers(number - 1) + fibonacci_numbers(number - 2)


user_number = int(input("Please enter any integer -> "))

print(f'Task 4 - Fibonacci number №{user_number} -> {fibonacci_numbers(user_number)}')


# Task 5. Decorators
def main_decorator():
    print("Task 5 - Decorator ")


    def tomato():
        print('tomato')

    def meat():
        print('meat')

    def cheese():
        print('cheese')

    def bread():
        print('bread')

    return tomato(), meat(), cheese(), bread()


def main_func():
    return None


main_decorator()
