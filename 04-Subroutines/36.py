tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

def suma(tab):
    s = 0
    for val in tab:
        if isinstance(val, int):
            s += val
        else:
            s += suma(val)
    return s


print(suma(tab))