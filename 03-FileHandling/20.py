tablica = []
with open('numbers.txt', 'r') as tekstowy1:
    for linia in tekstowy1:
        if(int(linia) % 2 == 0 and int(linia)>=0):
            tablica.append(linia)
with open('evennumbers.txt', 'w') as tekstowy2:
    for x in tablica:
        tekstowy2.write(x)