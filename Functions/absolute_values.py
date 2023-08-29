list_of_strings = input().split()
list_of_numbers = []

for num in list_of_strings:
    number = float(num)
    list_of_numbers.append(number)

list_of_absolute_values = []
for num in list_of_numbers:
    absolute_num = abs(num)
    list_of_absolute_values.append(absolute_num)

print(list_of_absolute_values)

