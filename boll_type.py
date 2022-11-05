# 1

comparison_correction: bool = 3 != 5
print(comparison_correction)

# 2

comparison_list_1: bool = 5 == 5
print(comparison_list_1)

comparison_list_2: bool = 5 <= 5
print(comparison_list_2)

comparison_list_3: bool = 5 >= 5
print(comparison_list_3)

comparison_list_4 = bool(5 <= 5 and 5 >= 5)
print(comparison_list_4)

comparison_list_5 = bool(5 <= 5 or 5 >= 5)
print(comparison_list_5)

# 3

logical_sequence_1 = True and True or False
print(logical_sequence_1)
logical_sequence_2 = True and (True or False)
print(logical_sequence_2)
logical_sequence_3 = True and not(True and False)
print(logical_sequence_3)
logical_sequence_4 = True and True and not False
print(logical_sequence_4)
logical_sequence_5 = not(True and True and False)
print(logical_sequence_5)

# 4

bool_none = bool(None)
bool_number = bool(7)
print(bool_none)
print(bool_number)
print(bool_none == bool_number)
# False - bool of None is False, bool of any number except 0 is True

bool_empty_str = bool(" ")
bool_expression = bool(10 - 1)
print(bool_empty_str)
print(bool_expression)
print(bool_empty_str == bool_expression)
# True - bool of empty string is True, bool of any number except 0 is True

bool_logical_operation = bool(True or False)
bool_function_print = bool(print("some text"))
print(bool_logical_operation)
print(bool_function_print)
print(bool_logical_operation == bool_function_print)
# False - bool of such logical operation is True, bool of print is False

bool_type_none = bool(type(None))
print(bool_type_none)
bool_id_none = bool(id(None))
print(bool_id_none)
print(bool_type_none == bool_id_none)
# True - bool of type function is True, bool of id function is True
