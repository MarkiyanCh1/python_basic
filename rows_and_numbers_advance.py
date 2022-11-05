user_name = input("Enter your name: ")
without_space = user_name.strip()
capital_letter = without_space.capitalize()
result = f"Hello {capital_letter}, nice to meet you!"
print(result)
print(f"Number of characters in the name: {len(without_space)}")
print(capital_letter[::-1])
