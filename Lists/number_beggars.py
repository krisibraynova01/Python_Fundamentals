string_of_integers = input().split(', ')
count_of_beggars = int(input())
list_money = []
counter_beggar = 0

for beggar in range(count_of_beggars):
    current_sum = 0
    for index in range(counter_beggar, len(string_of_integers), count_of_beggars):
        current_sum += int(string_of_integers[index])
        list_money.append(current_sum)
        counter_beggar += 1

print(list_money)
