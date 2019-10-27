# Program obliczy sumę i średnią arytmetyczną dowolnej ilości liczb wprowadzonych z klawiatury. 
# Wprowadzenie liczby 0 kończy wprowadzanie liczb.

b = 0
suma = 0
while True:    
    a = int(input('Podaj liczbę: '))
    if a == 0:
        srednia = suma/b
        break
    b += 1
    suma += a
print(f'REZULTAT: Liczb: {b}, Suma={suma}, Średnia={srednia}')
