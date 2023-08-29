line = input()
products = {}

while line != 'statistics':
    key, value = line.split(": ")
    value = int(value)
    if key not in products:
      products[key] = value
    else:
        products[key] += value

    line = input()

print('Products in stock:')

for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")






