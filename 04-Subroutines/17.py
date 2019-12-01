from random import randint
tab = []
def rzutKostka():
    tab.append(randint(1, 6))
    
for _ in range(3):
    rzutKostka()

print(f'Wyrzucone oczka: {tab[0]} {tab[1]} {tab[2]}\n Suma oczek: {sum(tab)}')