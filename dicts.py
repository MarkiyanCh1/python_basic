# Part 1
ascii_dict = {i: chr(i) for i in range(0, 128)}

print(ascii_dict)

# Part 2
alphabet = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
    "o": 15, "p": 16, "q": 17, "r": 18,  "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
}
word = list(input("Write a word: "))
step = int(input("Enter integer number: "))
letter_index = []
for letter in word:
    letter_index.append(alphabet.get(letter))
cypher_word = ""
for letter in letter_index:
    if letter + step < 26:
        for key, value in alphabet.items():
            if letter + step == value:
                cypher_word += key
    else:
        for key, value in alphabet.items():
            if letter + step - 26 == value:
                cypher_word += key

print(cypher_word)
