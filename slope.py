# file: slope.py
# joelDay

# This program prompts the user to click two points and draws a line
# between them and displays a calculated slope
from graphics import *

def clicks():
  p = win.getMouse()
  x, y = p.getX(), p.getY()
  p.draw(win)
  label = Text(Point(x + offset, y + offset), labelText).draw(win)
  click = Text(clickLabelLocation, clickLabelText % (x, y))
  click1.setSize(15)
  click1.draw(win)

clicks()


def main():

  WINDOW_WIDTH = 500
  WINDOW_HEIGHT = 500

  # Define window & Assets
  win = GraphWin("Joel's Slope Delivery System", WINDOW_WIDTH, WINDOW_HEIGHT)
  win.setCoords(0.0, 0.0, 100, 100)
  win.setBackground("snow")

  # Make a background grid
  for i in range(0, 101, 10):
    gridh = Line(Point(0, i), Point(WINDOW_WIDTH, i))
    gridh.setFill("LightSkyBlue1")
    gridh.draw(win)

    gridv = Line(Point(i, 0), Point(i, WINDOW_HEIGHT))
    gridv.setFill("LightSkyBlue1")
    gridv.draw(win)

  # Define text and output assetts
  header = Text(Point(50,90), "Click any two points")
  header.setSize(25)
  header.draw(win)

  # Handle first coordinates
  offset = -2
  labelText = "1."
  clickLabelLocation = Point(12,20)
  clickLabelText = "Point 1: (%d, %d)"

  p = win.getMouse()
  x, y = p.getX(), p.getY()
  p.draw(win)
  label = Text(Point(x + offset, y + offset), labelText).draw(win)
  click = Text(clickLabelLocation, clickLabelText % (x, y))
  click1.setSize(15)
  click1.draw(win)

  p1 = p
  x1, y1 = x, y

  # Handle second coordinates
  offset = +2
  labelText = "2."
  clickLabelLocation = Point(88,20)
  clickLabelText = "Point 2: (%d, %d)"

  p = win.getMouse()
  x, y = p.getX(), p.getY()
  p.draw(win)
  Text(Point(x + offset, y + offset), labelText).draw(win)
  click = Text(clickLabelLocation, clickLabelText % (x, y))
  click2.setSize(15)
  click2.draw(win)

  p2 = p
  x1, y1 = x, y

  # Draw the line
  Line(p1, p2).draw(win)

  # Calculate slope
  slope = (y2 - y1) / (x2 - x1)
  slope = round(slope, 1)

  # Output slope
  output2 = Text(Point(50, 10), "The slope of the line is: %1.1f." % (slope))
  output2.setSize(20)
  output2.draw(win)
  header.setText("Click anywhere to close")

  # Close the window
  win.getMouse()
  win.close()

main()
