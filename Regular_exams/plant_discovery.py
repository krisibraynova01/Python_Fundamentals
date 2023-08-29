n = int(input())

dict = {}

for _ in range(n):
    line = input().split('<->')
    plant = line[0]
    rarity = int(line[1])

    if plant not in dict:
        dict[plant] = {'rarity': rarity}
    else:
        dict[plant]['rarity'] = rarity

command = input()

while command != 'Exhibition':
    command_args = command.split(': ')
    plant = command_args[1]

    if 'Rate' in command_args:

        rating = int(command_args[2])



