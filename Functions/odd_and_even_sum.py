def sum(n):
    even_sum = 0
    odd_sum = 0
    for index in range(len(single_number)):
        current_num = int(single_number[index])
        if current_num % 2 == 0:
            even_sum += current_num
        elif current_num % 2 != 0:
            odd_sum += current_num
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

single_number = input()
result = sum(single_number)
print(result)
