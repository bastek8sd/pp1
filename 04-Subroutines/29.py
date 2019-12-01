import statistics

def mediana(table):
    print(f'Mediana: {statistics.median(tab)}')

def dominanta(table):
    table.sort()
    # max() - znajdź największą wartość
    # set() - przekonwertuj listę na set (unikalne wartości)
    # key - funkcja po której max() będzie porównywał
    # key=table.count - wyszukaj największej liczby dla której table.count(liczba) jest największa - np. dla 1 (w secie) table.count(1) (ile razy w table występuje liczba 1)
    return max(set(table), key=table.count)

tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]

print('Liczby: {}'.format(' '.join([str(i) for i in tab])))
mediana(tab)
print(f'Dominanta: {dominanta(tab)}')

