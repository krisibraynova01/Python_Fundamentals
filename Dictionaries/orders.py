command = input()
price_by_product = {}
quantity_by_product = {}

while command != 'buy':
    products = command.split()
    product = products[0]
    price = float(products[1])
    quantity = int(products[2])

    if product in price_by_product:
        price_by_product[product] = price
        quantity_by_product[product] += quantity
    else:
        price_by_product[product] = price
        quantity_by_product[product] = quantity

    command = input()

for product in price_by_product.keys():
    price = price_by_product[product]
    quantity = quantity_by_product[product]
    total_price = price * quantity

    print(f"{product} -> {total_price:.2f}")




