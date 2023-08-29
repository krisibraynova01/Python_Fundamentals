n = int(input())

sum_of_symbols = 0
for _ in range(n):
    symbol = input()

    sum_of_symbols += ord(symbol)

print(f'The sum equals: {sum_of_symbols}')