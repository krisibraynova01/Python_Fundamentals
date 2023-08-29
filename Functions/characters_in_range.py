def char_between(chr1, chr2):
    char_between = []
    for char in range(ord(chr1) + 1, ord(chr2)):
        char_between.append(chr(char))
    return char_between

first_char = input()
second_char = input()
result = char_between(first_char, second_char)
print(" ".join(result))