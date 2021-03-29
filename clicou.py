from graphics import *

def clicou_no_retangulo(ponto_1, ponto_2, click):

   window = GraphWin("Prog1 UFCG", 320, 200)

   r = Rectangle(Point(ponto_1,ponto_2))

   r.setFill("white")

   r.draw(window)

clicou_no_retangulo(100, 200, 50)
