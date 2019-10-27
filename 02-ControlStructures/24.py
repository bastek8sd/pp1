imiona = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]

tmp = 0
imie_index = None
for i in imiona:
    if len(i) > tmp:
        tmp = len(i)
        imie_index = imiona.index(i)
print(f'Najdłuższe imię: {imiona[imie_index]}')    