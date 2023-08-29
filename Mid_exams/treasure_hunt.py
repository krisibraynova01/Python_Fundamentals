string = input().split('|')

num_room = 0
health = 100
MAX_HEALTH = health
bitcoins = 0
for room in string:
    num_room += 1
    command, amount = room.split()
    amount = int(amount)
    if command == 'potion':
        if health + amount > 100:
            print(f'You healed for {MAX_HEALTH - health} hp.')
            health = MAX_HEALTH
        else:
            print(f'You healed for {amount} hp.')
            health += amount
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += amount
        print(f'You found {amount} bitcoins.')
    else:
        health -= amount
        if health > 0:
            print(f'You slayed {command}')
        else:
            print(f'You died! Killed by {command}')
            print(f'Best room: {num_room}')
            exit()

print("You've made it!")
print(f'Bitcoins: {bitcoins}')
print(f'Health: {health}')






