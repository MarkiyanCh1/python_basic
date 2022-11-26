user_string = input("Please enter any text -> ")
every_third_word = ', '.join(user_string.split()[2::3])

print(f"{every_third_word = }")

original_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
result_list = [element if isinstance(element, float)
               else element if (isinstance(element, int) and element % 2 == 0)
               else element ** 2 if (isinstance(element, int) and element % 2 != 0)
               else str(int(element) * 3) if (isinstance(element, str) and element.isdigit())
               else -1 for element in original_list
               ]

print(f"{original_list = }")
print(f"{result_list = }")
