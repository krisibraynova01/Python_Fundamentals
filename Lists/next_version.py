version_string = [int(x) for x in input().split(".")]

version_string[-1] += 1
for index in range(len(version_string) - 1, -1, -1):

    if version_string[index] > 9:
        version_string[index] = 0
        if index - 1 >= 0:
            version_string[index - 1] += 1



print('.'.join(str(x) for x in version_string))

