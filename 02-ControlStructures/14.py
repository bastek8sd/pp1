wiek = int(input('Podaj wiek psa w ludzkich latach: '))
      
if wiek <= 2:
    wiek_psi = wiek*10.5
else:
    wiek_psi = 21 + (wiek-2)*4
print(f'Wiek psa w psich latach wynosi: {wiek_psi} lata')
