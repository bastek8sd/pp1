limit = int(input("Podaj limit prędkości km/h:"))
velocity = int(input("Podaj prędkość pojazdu:"))

oblicz = (velocity - limit) * 5 + (velocity - limit - 10) * 10

print('Do zapłaty:')
if oblicz>0:
    print(oblicz)
else:
    print(0)
