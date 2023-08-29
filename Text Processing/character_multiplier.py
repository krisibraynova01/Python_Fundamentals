strings = input().split()
str1 = strings[0]
str2 = strings[1]

min_len = min(len(str1), len(str2))
result = 0
for index in range(min_len):
    first_word_char = str1[index]
    second_word_char = str2[index]
    result += ord(first_word_char) * ord(second_word_char)

for index in range(min_len, len(str1)):
    result += ord(str1[index])

for index in range(min_len, len(str2)):
    result += ord(str2[index])

print(result)



