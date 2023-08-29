n = int(input())

for i in range(1, n+1):
    is_special = False
    num_as_str = str(i)
    sum_digits = 0
    for char in num_as_str:
        sum_digits += int(char)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True

    print(f'{num_as_str} -> {is_special}')

