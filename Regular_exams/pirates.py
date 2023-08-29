line = input()
dict = {}

while line != 'Sail':
    command_args = line.split('||')

    city = command_args[0]
    population = int(command_args[1])
    gold = int(command_args[2])

    if city not in dict:
        dict[city] = {'population': {population}, 'gold': {gold}}
    else:
        dict[city]['population'] += population
        dict[city]['gold'] += gold
    line = input()

line = input()

while line != 'End':
    command_args = line.split('=>')
    city = command_args[1]
    if 'Plunder' in command_args:
        people = int(command_args[2])
        gold = int(command_args[3])
        dict[city]['population'] -= people
        dict[city]['gold'] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")







