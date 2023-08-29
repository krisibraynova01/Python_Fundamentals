single_line = input().split()

products = {}

for element in range(0, len(single_line), 2):
    key = single_line[element]
    value = int(single_line[element+1])

    products[key] = value

print(products)
