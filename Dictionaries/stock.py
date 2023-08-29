products_and_quantities = input().split()
stock = {}


for i in range(0, len(products_and_quantities),2):
    key = products_and_quantities[i]
    value = int(products_and_quantities[i+1])
    stock[key] = value

searched_product = input().split()
for product in searched_product:
    if product in stock:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")


