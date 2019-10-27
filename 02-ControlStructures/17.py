s_parz = 0
s_niep = 0
for i in range (1,51):
    if i % 2 == 0:
        s_parz += i
    else:
        s_niep += i
print(f'Suma liczb parzystych: {s_parz}\nSuma liczb nieparzystych: {s_niep}')