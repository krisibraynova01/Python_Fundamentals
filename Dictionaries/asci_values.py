list_of_characters = input().split(", ")
# values = {}
#
# for el in list_of_characters:
#     val = ord(el)
#     values[el] = val
#
# print(values)

print({char: ord(char) for char in list_of_characters})

