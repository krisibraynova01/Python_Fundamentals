first_string = input()
second_string = input()

result = first_string

for index in range(len(first_string)):
    if first_string[index] == second_string[index]:
        continue
    result = second_string[:index+1] + first_string[index+1:]
    print(result)