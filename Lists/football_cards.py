cards = input().split()

game_off = False
first_team_off_players = []
second_team_off_players = []


for i in cards:
    if i in first_team_off_players or i in second_team_off_players:
        continue
    cards_arguments = i.split('-')
    team_name = cards_arguments[0]
    player_number = cards_arguments[1]

    is_first_team = team_name == 'A'
    if is_first_team:
        first_team_off_players.append(i)
    else:
        second_team_off_players.append(i)

    if len(first_team_off_players) > 4 or len(second_team_off_players) > 4:
        game_off = True
        break


print(f'Team A - {11 - len(first_team_off_players)}; Team B - {11 - len(second_team_off_players)}')
if game_off:
    print('Game was terminated')

