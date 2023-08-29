group_size = int(input())
days = int(input())
coins = 0

from math import floor

for day in range(1, days + 1):
    coins += 50 - 2 * group_size
    if days % 10 == 0:
        group_size -= 2
    elif days % 15 == 0:
        group_size += 5
        coins -= 2 * group_size
    coins += 50 - 2 * group_size

    if days % 3 == 0:
        coins -= 3 * group_size
    if days % 5 == 0:
        coins += 20 * group_size
        if days % 3 == 0:
            coins -= 2 * group_size

coins_per_season = floor(coins / group_size)

print(f'{group_size} companions received {coins} coins each.')
