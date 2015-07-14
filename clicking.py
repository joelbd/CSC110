# file: clicking.py
# joelDay

from graphics import *
p1 = Point(50,150)
p2 = Point(450,350)

def main():

  win = GraphWin("New Big Window", 500,500)
  win.setBackground("yellow")

  rectangle = Rectangle(p1, p2)
  rectangle.setWidth(3)
  rectangle.setOutline("blue")
  rectangle.setFill("red")
  rectangle.draw(win)

  oval = Oval(p1, p2)
  oval.setOutline("green")
  oval.setFill("green")
  oval.draw(win)

main()
