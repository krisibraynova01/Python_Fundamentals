def action(num):
    return f'The minimum number is {min(num)} \nThe maximum number is {max(num)} \nThe sum number is: {sum(num)}'

numbers = [int(number) for number in input().split()]
print(action(numbers))