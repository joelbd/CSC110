# file: face.py
# joelDay

# This program creates a face and outputs to a window

from graphics import *

def main():

  win = GraphWin("The face of python", 500, 500)
  win.setBackground("blue")
  head = Oval(Point(100,50), Point(400,450))
  head.setFill("MediumOrchid4")
  head.draw(win)

  left_eye = Circle(Point(150,150), 10)
  left_eye.setFill("yellow")
  left_eye.draw(win)
  right_eye = Circle(Point(310,130), 35)
  right_eye.setFill("yellow")
  right_eye.draw(win)

  mouth = Line(Point(145,350), Point(270,350))
  mouth.draw(win)
  caption = Text(Point(100,450), "i R an mistaek")
  caption.setSize(25)
  caption.setFill("green3")
  caption.draw(win)

main()
