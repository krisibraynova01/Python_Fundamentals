num_of_pieces = int(input())
dict = {}

for _ in range(num_of_pieces):
    line = input().split('|')
    piece = line[0]
    composer = line[1]
    key = line[2]
    dict[piece] = {'composer': composer, 'key': key}


command = input()

while command != 'Stop':
    command_args = command.split('|')
    piece = command_args[1]

    if 'Add' in command_args:
        composer = command_args[2]
        key = command_args[3]
        if piece in dict:
            print(f"{piece} is already in the collection!")
        else:
            dict[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif 'Remove' in command_args:
        if piece in dict:
          del dict[piece]
          print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif 'ChangeKey' in command_args:
        new_key = command_args[2]
        if piece in dict:
            dict[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {dict[piece]['key']}!")
        else:
         print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for key, value in dict.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")




