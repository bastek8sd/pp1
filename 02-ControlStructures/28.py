
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

if a == 1:
    for x in range(0,b):
        print('*')
else:
    for x in range(0,a):
        print('*', end='')
    print()
    if b != 1:
        for x in range(0,b-2):
            print('*', end='')
            for y in range(0,a-2):
                print(' ', end='')
            print('*')
        for x in range(0,a):
            print('*', end='')
