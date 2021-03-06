# file: slope.py
# joelDay

# This program prompts the user to click two points and draws a line
# between them and displays a calculated slope
from graphics import *

def clicks(win, offset, clickLabelLocation, clickLabelText, labelText):
  p = win.getMouse()
  x, y = p.getX(), p.getY()
  p.draw(win)
  Text(Point(x + offset, y + offset), labelText).draw(win)
  click = Text(clickLabelLocation, clickLabelText % (x, y))
  click.setSize(15)
  click.draw(win)
  return p

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

  # Define text and output assets
  header = Text(Point(50,90), "Click any two points")
  header.setSize(25)
  header.draw(win)

  # Handle first coordinates
  p1 = clicks(win, -2, Point(12, 20), "Point 1: (%d, %d)", "1.")

  # Handle second coordinates
  p2 = clicks(win, +2, Point(88, 20), "Point 2: (%d, %d)", "2.")

  # Draw the line
  line = Line(p1, p2)
  line.setArrow("both")
  line.draw(win)

  # Calculate slope
  slope = (p2.getY() - p1.getY()) / (p2.getX() - p1.getX())
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
