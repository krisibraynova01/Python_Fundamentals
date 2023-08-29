lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_losted = 0
sword_losted = 0
shield_losted = 0
armor_break = 0
for games in range(1, lost_fights_count + 1):
    if games % 2 == 0:
        helmet_losted += 1
    if games % 3 == 0:
        sword_losted += 1
    if games % 2 == 0 and games % 3 == 0:
        shield_losted += 1
        if shield_losted % 2 == 0:
          armor_break += 1

    total_expenses = helmet_price * helmet_losted + sword_price * sword_losted + shield_price * shield_losted + armor_price * armor_break
print(f'Gladiator expenses: {total_expenses:.2f} aureus')
