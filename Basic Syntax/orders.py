num_of_orders = int(input())

total_price = 0
for i in range(num_of_orders):
  price_per_capsule = float(input())
  days = int(input())
  needed_capsules_per_day = int(input())

  if price_per_capsule < 0.01 or price_per_capsule > 100:
    continue

  if days < 1 or days > 31:
    continue

  if needed_capsules_per_day < 1 or needed_capsules_per_day > 2000:
    continue

  price = days * needed_capsules_per_day * price_per_capsule
  print(f'The price for the coffee is: ${price:.2f}')
  total_price += price


print(f'Total: ${total_price:.2f}')



