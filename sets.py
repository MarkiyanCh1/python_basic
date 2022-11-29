# Task 1

first_user_input = set(input('Please enter first text -> '))
second_user_input = set(input('Please enter second text -> '))

intersection_of_inputs = first_user_input.intersection(second_user_input)
symmetric_difference_of_inputs = first_user_input.symmetric_difference(second_user_input)
similar_letters_in_sets = {element for element in intersection_of_inputs if element.isalpha()}
unique_numbers_in_sets = {element for element in symmetric_difference_of_inputs if element.isdigit()}

print(f'List of letters that are present in both sets -> {similar_letters_in_sets}')
print(f'List of unique numbers in sets -> {unique_numbers_in_sets}')

# Task 2

# |= or update()
set1 = {1, 2, 3, 5, 6, 8, 9, 10}
set2 = {1, 2, 4, 5, 6, 9, 12}
set3 = {2, 5, 6, 9, 13, 7}
set1 |= set2 | set3  # Adds to set1 all elements from set2 and set3

print(f'{set1 = } <- update()')


# &= or intersection_update()
set4 = {1, 2, 3, 5, 6, 8, 9, 10}
set5 = {1, 2, 4, 5, 6, 9, 12}
set6 = {2, 5, 6, 9, 13, 7}
set4 &= set5 & set6  # Leaves in set4 only those elements that are in set5 and set6

print(f'{set4 = } <- intersection_update()')

# -= or difference_update()
set7 = {1, 2, 3, 5, 6, 8, 9, 10, 'a', 'b'}
set8 = {1, 2, 4, 5, 6, 9, 12}
set9 = {2, 5, 6, 9, 13, 7}
set7 -= set8 | set9  # Removes from set7 all elements included in set8 and set9

print(f'{set7 = } <- difference_update()')

# ^= or symmetric_difference_update()
set10 = {1, 2, 3, 5, 6, 8, 9, 10, 'a', 'b'}
set11 = {1, 2, 4, 5, 6, 9, 12}
set12 = {2, 5, 6, 9, 13, 7}
set10 ^= set11 | set12  # Adds to the set10 the elements that are in set10, set11 or set12, but not all at the same time

print(f'{set10 = } <- symmetric_difference_update()')
