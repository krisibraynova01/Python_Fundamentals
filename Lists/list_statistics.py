n = int(input())
list_positive = []
list_negative = []
count_positive = 0
sum_negative = 0
for i in range(n):
    num = int(input())
    if num >= 0:
        list_positive.append(num)
        count_positive += 1
    else:
        list_negative.append(num)
        sum_negative += num
print(list_positive)
print(list_negative)
print(f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')

