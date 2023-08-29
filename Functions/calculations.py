def solve(operator, a, b):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a // b
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b

op = input()
first_number = int(input())
second_number = int(input())

print(solve(op, first_number, second_number))



