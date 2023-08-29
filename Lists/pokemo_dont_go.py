sequence = [int(x) for x in input().split()]
sum = 0

while len(sequence) != 0:
    indexes = int(input())

    if indexes >= 0 and len(sequence) >= 0:
        popped = sequence.pop(indexes)

        for i in range(len(sequence)):
            if sequence[i] <= popped:
                sequence[i] += popped
            else:
                sequence[i] -= popped
    elif indexes < 0:
        popped = sequence.pop(0)
        sum += popped

        for i in range(len(sequence)):
            if sequence[i] <= popped:
                sequence[i] += popped
            else:
                sequence[i] -= popped

        value_of_the_last = sequence[-1]
        sequence.insert(0, value_of_the_last)

    elif (indexes > len(sequence) - 1):
        popped = sequence.pop(len(sequence) - 1)
        sum += popped

        for i in range(len(sequence)):
            if (sequence[i] <= popped):
                sequence[i] += popped
            else:
                sequence[i] -= popped

        valueOfTheFirst = sequence[0]
        sequence.append(valueOfTheFirst)

print(sum)









