# file: shapes_2a.py
# joelDay


from graphics import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

def main():
  # Create a window
  win = GraphWin("Window of Shapes", WINDOW_WIDTH, WINDOW_HEIGHT)
  win.setBackground("SkyBlue1")
  win.setCoords(0.0, 0.0, WINDOW_WIDTH, WINDOW_HEIGHT)

  rect = Rectangle(Point(50, WINDOW_HEIGHT - 50), Point(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT / 2 + 50))
  rect.setFill("light goldenrod")
  rect.setOutline("sienna4")
  rect.setWidth(5)
  rect.draw(win)

  oval = Oval(Point(WINDOW_WIDTH / 2 + 50, WINDOW_HEIGHT - 50), Point(WINDOW_WIDTH - 50, WINDOW_HEIGHT / 2 + 50))
  oval.setFill("light goldenrod")
  oval.setOutline("sienna4")
  oval.setWidth(5)
  oval.draw(win)

  triangle = Polygon(
    Point(50, 50),
    Point((WINDOW_WIDTH / 3) / 2, WINDOW_HEIGHT / 2 - 50),
    Point((WINDOW_WIDTH / 3) - 50, 50))
  triangle.setFill("light goldenrod")
  triangle.setOutline("sienna4")
  triangle.setWidth(5)
  triangle.draw(win)

  circle = Circle(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4,), WINDOW_HEIGHT / 4 - 50)
  circle.setFill("light goldenrod")
  circle.setOutline("sienna4")
  circle.setWidth(5)
  circle.draw(win)

  square = Rectangle(Point(WINDOW_WIDTH / 3 * 2 + 50, WINDOW_HEIGHT / 2 - 50), Point(WINDOW_WIDTH - 50, 50))
  square.setFill("light goldenrod")
  square.setOutline("sienna4")
  square.setWidth(5)
  square.draw(win)

main()
