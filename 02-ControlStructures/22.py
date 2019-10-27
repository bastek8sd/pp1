table = [15,8,31,47,2,19]

i = 0
s = 0
for x in table:
    if x % 2 != 0:
        s += x
        i += 1
sr =  s/i
print(f'Średnia arytmetyczna liczb nieparzystych wynosi: {sr}')