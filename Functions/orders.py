def calculated_price(item, count):
    if item == 'coffee':
        return count * 1.50
    elif item == 'water':
        return count * 1.00
    elif item == 'coke':
        return count * 1.40
    elif item == 'snacks':
        return count * 2.00


product = input()
quality = int(input())
result = calculated_price(product, quality)
print(f'{result:.2f}')
