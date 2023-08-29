num_of_heroes = int(input())
dict = {}

for _ in range(num_of_heroes):
    line = input().split()
    hero_name = line[0]
    hit_points = int(line[1])
    mana_points = int(line[2])
    dict[hero_name] = {"HP": hit_points, "MP": mana_points}

line = input()
while line != 'End':

     command = line.split(" - ")

     if "CastSpell" in command:
         mana_points_need = int(command[2])
         spell_name = command[3]
         if dict[hero_name]["MP"] >= mana_points_need:
            dict[hero_name]["MP"] -= mana_points_need
            print(f"{hero_name} has successfully cast {spell_name} and now has {dict[hero_name]['MP']} MP!")
         else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
     if "TakeDamage" in command:
        damage = int(command[2])
        attacker = command[3]
        dict[hero_name]["HP"] -= damage
        if dict[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dict[hero_name]['HP']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
     if "Recharge" in command:
        amount = int(command[2])
        if dict[hero_name]["MP"] + amount > 200:
            print(f"{hero_name} recharged for {200-dict[hero_name]['MP']} MP!")
            dict[hero_name]['MP'] = 200
        else:
            dict[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
     if "Heal" in command:
        amount = int(command[2])
        if dict[hero_name]["HP"] + amount > 100:
            print(f"{hero_name} recharged for {100 - dict[hero_name]['HP']} MP!")
            dict[hero_name]['HP'] = 100
        else:
            dict[hero_name]['HP'] += 100
            print(f"{hero_name} recharged for {amount} HP!")

        command = input()

for key, value in dict.items():
        print(f"{key}\n HP: {value['HP']}\n MP: {value['MP']}")












