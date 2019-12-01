txt = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'

def liczSamogl(txt):
    znaki = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
    temp = []
    for znak in znaki:
        temp.append(txt.count(znak))
    # łączenie 2 list na słownik klucz:wartość
    result = {znaki[i]: temp[i] for i in range(0, len(znaki))}

    return result


result = liczSamogl(txt)

# wypisywanie par ze słownika klucz(key):wartość(result[key])
for key in result:
    print(f'{key} : {result[key]}')