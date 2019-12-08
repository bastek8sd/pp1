import turtle
def drawSquare():
    osX = -100
    osY = 100
    pen = turtle.Turtle()
    pen.up()
    pen.setposition(osX, osY)
    pen.down()

    for x in range (4):          #Pętla duży kwadrat (4 prostokąty w rzędzie)
        for x in range (4):      #Pętla prostokąt
            for x in range(4):   #Pętla kwadrat
                pen.forward(100)
                pen.right(90)     # Rotate clockwise by 90 degrees
            osX += 100
            pen.setposition(osX, osY)
        osX -= 400
        osY -= 100
        pen.up()
        pen.setposition(osX, osY)
        pen.down()
        
    turtle.done()

def drawCircle(x, y, r):
    import turtle
    pen = turtle.Turtle()
    pen.penup()
    pen.setpos(x, y-r)
    pen.pendown()
    pen.circle(r)
    turtle.done()


def drawTriangle(x, y, m):
    import turtle
    pen = turtle.Turtle()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.seth(0)
    pen.right(60)
    for _ in range(1, 4):
        pen.forward(m)
        pen.right(120)
    turtle.done()


def drawStar():
    import turtle
    pen = turtle.Turtle()

    for i in range(10):
        pen.forward(70)
        if i % 2 == 0:
            pen.left(72)
        else:
            pen.right(144)

    turtle.done()


def drawFilledSquare(x, y, m, color='black', existing=None):
    if existing == None:
        import turtle
        pen = turtle.Turtle()
    else:
        pen = existing

    pen.penup()
    pen.setpos(x, y)
    pen.seth(0)
    pen.fillcolor(color)
    pen.pendown()
    pen.begin_fill()

    for _ in range(4):
        pen.forward(m)
        pen.right(90)

    pen.end_fill()

    if existing == None:
        turtle.done()


def drawChessboard(m):
    import turtle

    pen = turtle.Turtle()
    pen.speed(10)
    color = 'white'
    notcolor = 'black'

    for y in range(8, 0, -1):
        for x in range(8):
            drawFilledSquare(x * m, y * m, m, color, pen)
            if x != 7:
                color, notcolor = (notcolor, color)
    turtle.done()

#setposition()
#penup(), pendown()
#setheading()
