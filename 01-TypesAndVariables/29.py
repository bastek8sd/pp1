from random import randint

x = randint(1,6)
y = input('Podaj, ile oczek kostki wyrzucił komputer: ')

print(f'Komputer wyrzucił {x}')
if y == x:
    status_flag = True
else:
    status_flag = False
print(f'Zgadłeś: {status_flag}')