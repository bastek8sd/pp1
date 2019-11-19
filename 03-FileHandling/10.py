suma = 0
with open('numbers.txt','r') as file:
    for line in file:
        suma = suma + int(line)
print(suma)