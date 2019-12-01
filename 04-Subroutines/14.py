tab = [15, 38, 7, 23, 14]
def wystepuje(liczba, tablica):
    print(f'Liczba: {liczba}')
    print(f'Tablica: {tablica}')
    if liczba in tablica:
        print(f'Rezultat: Podana liczba występuje w tablicy')
    else:
        print(f'Rezultat: Podana liczba nie występuje w tablicy')
    
wystepuje(23, tab)