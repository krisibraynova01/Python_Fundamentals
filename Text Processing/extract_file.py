file_name = input().split("\\")
file = file_name[-1]
info = file.split(".")
name = info[0]
type_file = info[-1]


print(f'File name: {name}')
print(f'File extension: {type_file}')






