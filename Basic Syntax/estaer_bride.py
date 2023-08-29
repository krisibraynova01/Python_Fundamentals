budget = float(input())

flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25

loaf_price = flour_price + eggs_price + milk_price

loafs_counter = 0
colored_eggs = 0
while loaf_price <= budget:
    loafs_counter += 1
    budget -= loaf_price
    colored_eggs += 3

    if loafs_counter % 3 == 0:
        colored_eggs -= (loafs_counter - 2)

print(f'You made {loafs_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
