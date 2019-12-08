import turtle

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



#setposition()
#penup(), pendown()
#setheading()