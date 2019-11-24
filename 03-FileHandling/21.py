tablica = []
suma = 0
with open('numbersinrows.txt', 'r') as file:
    for line in file:
        tablicaLini = line.split(",")
        for x in tablicaLini:
            tablica.append(x)
            suma = suma + int(x)
            
print(f'Ilość liczb w pliku: {len(tablica)}\n Suma liczb w pliku: {suma}')
