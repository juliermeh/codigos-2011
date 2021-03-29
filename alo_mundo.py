from graphics import *

window = GraphWin("Prog1 UFCG", 320, 200)

c = Circle(Point(160,100), 70)

c.setFill("white")

c.draw(window)

texto = Text(Point(160,100),"Hello World!")

texto.draw(window)

click = window.getMouse()

window.close()
