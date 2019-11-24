tablica = []
with open('universities.txt', 'r') as tekstowy1:
    for linia in tekstowy1:
        tablica.append(linia.strip('"'))
tablica.sort()
with open('universities.txt', 'w') as tekstowy2:
    for x in tablica:
        tekstowy2.write(f'{x}\n')