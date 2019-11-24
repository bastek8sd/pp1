import re
with open('land.txt', 'r') as file:
    tmp = re.findall('\d', file.read())
tmp = [int(i) for i in tmp]
print(sum(tmp))