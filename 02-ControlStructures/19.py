x = int(input('Podaj wartość N: '))
print('Ciąg arytmetyczny o różnicy 3: ', end='')
for i in range(1, 3*(x), 3):
    print(i, end=', ')
