import re

text = input()


result = re.findall(r'\b_([A-Za-z0-9]+)\b', text)

print(','.join(result))