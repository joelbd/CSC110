# file: slope.py
# joelDay

# This program prompts the user to click two points and draws a line
# between them and displays a calculated slope
from graphics import *

def main():

  # Define window & Assets
  win = GraphWin("Joel's Slope Delivery System", 500,500)
  win.setCoords(0.0,0.0,100,100)
  win.setBackground("snow")

  # Make a background grid
  for i in range(0,101,10):
    gridh = Line(Point(0,i), Point(500,i))
    gridh.setFill("LightSkyBlue1")
    gridh.draw(win)
    gridv = Line(Point(i,0), Point(i,500))
    gridv.setFill("LightSkyBlue1")
    gridv.draw(win)

  # Define text and output assetts
  header = Text(Point(50,90), "Click any two points")
  header.setSize(25)
  header.draw(win)

  # Handle first coordinates
  p1 = win.getMouse()
  x1, y1 = p1.getX(), p1.getY()
  p1.draw(win)
  label1 = Text(Point(x1 - 2, y1 - 2), "1.").draw(win)
  click1 = Text(Point(12,20), "Point 1: (%d, %d)" % (x1,y1))
  click1.setSize(15)
  click1.draw(win)

  # Handle second coordinates
  p2 = win.getMouse()
  x2,y2 = p2.getX(), p2.getY()
  p2.draw(win)
  Text(Point(x2 + 2, y2 + 2), "2.").draw(win)
  click2 = Text(Point(88,20), "Point 2: (%d, %d)" % (x2,y2))
  click2.setSize(15)
  click2.draw(win)

  # Draw the line
  Line(p1, p2).draw(win)

  # Calculate slope
  slope = (y2 - y1) / (x2 - x1)
  slope = round(slope, 1)

  # Output slope
  output2 = Text(Point(50,10), "The slope of the line is: %1.1f." % (slope))
  output2.setSize(20)
  output2.draw(win)
  header.setText("Click anywhere to close")

  # Close the window
  win.getMouse()
  win.close()

main()
