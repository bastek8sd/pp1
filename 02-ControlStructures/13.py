x = float(input('Podaj liczbę x: '))
y = float(input('Podaj liczbę y: '))
if x == 0 and y == 0:
    print(f'Punkt P({x},{y}) znajduje się w początku układu współrzędnych.')
elif x == 0:
    print(f'Punkt P({x},{y}) znajduje się na osi X') 
elif y == 0:
    print(f'Punkt P({x},{y}) znajduje się na osi Y')
elif x > 0 and y > 0:
    print(f'Punkt P({x},{y}) znajduje się w I ćw')
elif x < 0 and y > 0:
    print(f'Punkt P({x},{y}) znajduje się w II ćw')
elif x < 0 and y < 0:
    print(f'Punkt P({x},{y}) znajduje się w III ćw')
elif x > 0 and y < 0:
    print(f'Punkt P({x},{y}) znajduje się w IV ćw')
