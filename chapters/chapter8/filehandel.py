file = open('demo.txt', 'r')

fre = file.readlines()

print(fre[0])
print(fre[1].split('=')[1])

# ffile = open('demo.txt', 'r').read()

# variable = 'pwc'

# ini = ffile.find(variable)+(len(variable)+1)

# rest = ffile[ini:]

# search_enter = rest.find('\n')

# print(search_enter)

# number = int(rest[:search_enter])

# print("value:", number)
