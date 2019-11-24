tablica = []
with open('numbers.txt', 'r') as tekstowy:
    for linia in tekstowy:
        tablica.append(linia)
tablica.sort()
for x in tablica:
    print(x, end='')