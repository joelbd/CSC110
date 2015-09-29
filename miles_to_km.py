# file: miles_to_km.py
# joelDay

# This program provides a GUI interface that will take a distance in miles
# and convert it to kilometers
from graphics import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

def main():

  # Define Window
  win = GraphWin("Convert Miles To Kilometers", WINDOW_WIDTH, WINDOW_HEIGHT)
  win.setBackground("Light Gray")
  win.setCoords(0.0, 0.0, WINDOW_WIDTH, WINDOW_HEIGHT)

  # Define prompt for input
  header = Text(Point(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50), "Convert your miles to Kilometers!")
  header.setSize(30)
  header.setFill("Dark Slate Gray")
  header.setStyle("bold")
  header.draw(win)

  # Handle miles input
  miles = Entry(Point(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 150), 10)
  miles.setSize(30)
  miles.setText("Enter miles")
  miles.setStyle("bold")
  miles.setFill("Dark Slate Blue")
  miles.draw(win)

  # Create CTA button
  button = Text(Point(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), "Click to convert.")
  button.setSize(20)
  button.setFill("Dark Slate Blue")
  button.draw(win)
  win.getMouse()

  # Render output assets
  rectangle = Rectangle(Point(50, WINDOW_HEIGHT // 2 - 50), Point(WINDOW_WIDTH - 50, 50))
  rectangle.setFill("Forest Green")
  rectangle.setOutline("white")
  rectangle.setWidth(15)
  rectangle.draw(win)

  # Convert and output distance in km
  enteredText = miles.getText()
  mi = eval(enteredText)
  km = mi * 1.609
  output = Text(Point(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 450), "%1.1f miles is %1.1f km" % (mi, km))
  output.setSize(36)
  output.setFill("white")
  output.draw(win)
  button.undraw()
  header.setText("Click anywhere to close.")

  # Exit the program
  win.getMouse()
  win.close()

main()
