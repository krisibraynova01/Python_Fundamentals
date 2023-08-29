prices = input()
total_price = 0
price_without_taxes = 0

while prices != 'special' or prices != 'regular':
    price = float(prices)
    price_without_taxes += price
    taxes = price_without_taxes * 0.20
    prices = str(input())
    if prices == 'special':
        total_price = (price_without_taxes + price) - (price_without_taxes + price) * 0.1
    else:
        total_price = (price_without_taxes + price)
    if price < 0:
        print('Invalid price!')
        prices = input()
        continue
    if total_price == 0:
        print("Invalid order!")

print(f"Congratulations you've just bought a new computer! \n  Price without taxes: {price_without_taxes:.2f}$ Taxes: {taxes:.2f}$ \n ----------- \n Total price: {total_price}$" )



