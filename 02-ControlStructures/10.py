# czy liczba jest zarówno dodatnia jak i nieparzysta

x = int(input('Podaj liczbę: '))
if x > 0 and x % 2 == 1:
    print('Podana liczba jest zarówno dodatnia jak i nieparzysta')
else:
    print('Podana liczba nie spełnia warunków')
