n = int(input())
keyword = input()
all_words = []
keywords = []

for _ in range(n):
    string = input()
    all_words.append(string)
    if keyword in string:
        keywords.append(string)

print(all_words)
print(keywords)

