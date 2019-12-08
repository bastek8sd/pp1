import shapes

mode = input('Wybierz podpunkt a-e: ')
if mode == 'a':
    print('Okrąg x,y promień r')
    x = int(input('x: '))
    y = int(input('y: '))
    r = int(input('r: '))
    shapes.drawCircle(x, y, r)
elif mode == 'b':
    print('Trójkąt x,y bok m')
    x = int(input('x: '))
    y = int(input('y: '))
    m = int(input('m: '))
    shapes.drawTriangle(x, y, m)
elif mode == 'c':
    shapes.drawStar()
elif mode == 'd':
    shapes.drawFilledSquare(50, 50, 100)
else:
    shapes.drawChessboard(25)