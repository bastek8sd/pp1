import math

# ustawianie wartości promienia i liczby pi
pi = math.pi
r = 5

# obliczania
P = pi*r**2
L = 2*pi*r

print("""Pole koła o promieniu {0} wynosi {1}
Obwód koła o promieniu {0} wynosi {2}""".format(r,P,L))
