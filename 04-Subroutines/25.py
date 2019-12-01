imiona = ['Janek', 'Ania', 'Wojtek', 'Zosia']

def jestImie(imie, imiona):
    print(f'Imiona: {imiona}')
    print(f'Imię: {imie}')
    if imie in imiona:
        print(f'Rezultat: imię zawarte jest w wykazie imion')
    else:
        print(f'Rezultat: imię nie jest zawarte w wykazie imion')
        
jestImie('Wojtek', imiona)