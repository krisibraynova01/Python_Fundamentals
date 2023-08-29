line = input()

dict_by_force_side = {}
dict_by_force_user = {}

while line != 'Lumpawaroo':
    if " | " in line:
        info = line.split(" | ")
        force_side = info[0]
        force_user = info[1]

        if force_side not in dict_by_force_side:
            dict_by_force_side[force_side] = []
        if force_user not in dict_by_force_user:
            dict_by_force_user[force_user] = force_side
            dict_by_force_side[force_side].append(force_user)

    else:
        info = line.split(" -> ")
        force_user = info[0]
        force_side = info[1]
        if force_side not in dict_by_force_side:
            dict_by_force_side[force_side] = []
        if force_user in dict_by_force_side:
            old_side = dict_by_force_side[force_user]
            dict_by_force_side[old_side].remove(force_user)
       





