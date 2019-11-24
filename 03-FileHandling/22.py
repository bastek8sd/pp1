tablica = []
i=0
with open('students.txt', 'r') as file:
    for line in file:
        tablicaLini = line.split(",")
        i = i+1
        if(i>1):
            if(int(tablicaLini[2]) < 30):
                for x in tablicaLini:
                    if(x == tablicaLini[0] or x == tablicaLini[1] or x == tablicaLini[4]):
                        tablica.append(x)
    print(tablica[0], tablica[1], tablica[2])
    print(tablica[3], tablica[4], tablica[5])
    print(tablica[6], tablica[7], tablica[8])
