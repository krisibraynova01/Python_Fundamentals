line = input()
items = {}

while line != 'stop':
    amount = int(input())
    if line not in items:
        items[line] = amount
    else:
        items[line] += amount

    line = input()




for res, qua in items.items():
    print(f"{res} -> {qua}")

