def sum_numbers(num1, num2):
    return num1 + num2

def substract(sum_num,num3):
    return sum_num - num3

first_number = int(input())
second_number = int(input())
third_number = int(input())
result1 = sum_numbers(first_number, second_number)
result2 = substract(sum_numbers(first_number, second_number), third_number)

print(result2)

