needed_amount = float(input())
count_of_battles = int(input())
collect_experience = 0
counter_battles = 0

for i in range(1, count_of_battles + 1):
    counter_battles += 1
    experience = float(input())
    if counter_battles % 15 == 0:
        experience = experience + (experience + 0.05)
    if counter_battles % 3 == 0:
        experience = experience + (experience * 0.15)
    if counter_battles % 5 == 0:
        experience = experience - (experience * 0.10)
    collect_experience += experience
    if collect_experience >= needed_amount:
     print(f'Player successfully collected his needed experience for {counter_battles} battles.')
     exit()

if collect_experience < needed_amount:
    print(f'Player was not able to collect the needed experience, {(needed_amount - collect_experience):.2f} more needed.')

