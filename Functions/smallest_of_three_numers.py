def smallest_number(first_num, second_num, third_num):
    if first_num < second_num and first_num < third_num:
        return first_num
    elif second_num < first_num and second_num < third_num:
        return second_num
    elif third_num < first_num and third_num < second_num:
        return third_num


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_number(first_number, second_number, third_number))