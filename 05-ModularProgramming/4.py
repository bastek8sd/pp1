from math import sqrt, pow, pi, factorial, trunc

x = 3.7
y = 4

sqrtX = sqrt(x)
potegaxy = pow(x,y)
sqrtXzY = pow(x, 1/y)
poleKola = pi*pow(y, 2)
silnia = factorial(y)
najLiczbaX = trunc(x)

print(f'Pierwiastek kwadratowy z {x} wynosi {sqrtX}')
print(f'{x} do potęgi {y} wynosi {potegaxy}')
print(f'Pierwiastek y-tego ({y}) stopnia z x ({x}) wynosi {sqrtXzY}')
print(f'Pole koła o promieniu {y} wynosi {poleKola}')
print(f'Silnia {y} wynosi {silnia}')
print(f'Największą możliwa liczba całkowita, mniejsza bądź równa {x} wynosi {najLiczbaX}')