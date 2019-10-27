
a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))

p = (a + b + c)/2
S = (p*(p-a)*(p-b)*(p-c))**(1/2)
print(f'Pole trójkąta wynosi {S}')
