cards = input().split()
count_shaffles = int(input())
left_half = []
right_half = []

for index in range(count_shaffles):
    new_cards = []
    half_part = int(len(cards) / 2)
    left_half = cards[0:half_part]
    right_half = cards[half_part::]
    for card in range(len(left_half)):
        new_cards.append(left_half[card])
        new_cards.append(right_half[card])
    cards = new_cards

print(cards)


