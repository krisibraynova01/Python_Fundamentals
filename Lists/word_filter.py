text = [x for x in input().split()]
#list = []
#for string in text:
#if len(string) % 2 == 0:
        #list.append(string)

#print('\n'.join(string for string in list))

word_filter = [word for word in text if len(word) % 2 == 0]
print('\n'.join(word_filter))



