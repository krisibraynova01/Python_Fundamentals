num_of_decorations = int(input())
days_left_until_christmas = int(input())
days_counter = 0
points = 0
total_price = 0

for i in range(days_left_until_christmas,0,-1):
    days_counter += 1
    if days_counter % 2 == 0:
        total_price += num_of_decorations * 2
        points += 5
    if days_counter % 3 == 0:
        total_price += (num_of_decorations * 5) + (num_of_decorations * 3)
        points += 3 + 10
    if days_counter % 5 == 0:
        total_price += num_of_decorations * 15
        points += 17
        if days_counter % 3 == 0:
            points += 30
    if days_counter % 10 == 0:
        points -= 20
        total_price += 5+3+15

