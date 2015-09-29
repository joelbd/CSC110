# birthday_functions.py
# joelDay

from graphics import *

# Define window & window variables.
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
midhoriz = WINDOW_WIDTH / 2
midvert = WINDOW_HEIGHT / 2

def createWindow():
  # Create window.
  win = GraphWin("Bouncing Ball", WINDOW_WIDTH, WINDOW_HEIGHT)
  win.setCoords(0.0, 0.0, WINDOW_WIDTH, WINDOW_HEIGHT)
  win.setBackground("light goldenrod")

# Create bouncing animation.
def bounce(ball, repeats, ballReturn):

  for j in range(repeats):

    for i in range(12):
      ball.move(2.5, -5.0)
      time.sleep(.012)

    for i in range(12):
      ball.move(2.5, 5.0)
      time.sleep(.012)

  for i in range(ballReturn):
    ball.move(-15.0, 0)
    time.sleep(.02)

def singSong(win, bounce,)
def main():


  # Handle name input
  name = Entry(Point(midhoriz, WINDOW_HEIGHT - 40), 20)
  name.draw(win)
  caption = Text(Point(midhoriz, WINDOW_HEIGHT - 75), "Type your name and click to continue")
  caption.setSize(20)
  caption.draw(win)
  win.getMouse()

  # Remove text field and prompt. Replace with celebratory image.
  caption.undraw()
  name.undraw()
  enteredText = name.getText()
  cake = Image(Point(midhoriz, midvert + 20), "birthday.gif")
  cake.draw(win)

  # Generate ball.
  ball = Circle(Point(40, 160), 10)
  ball.setFill("LightSkyBlue1")
  ball.draw(win)

  # Create lyrics template.
  lyrics = Text(Point(225, 75), "Hap - py  Birth-day   To   You")
  lyrics.setFill("red3")
  lyrics.setSize(25)
  lyrics.setStyle("bold")
  lyrics.draw(win)

  # Bounce the ball with accompanying lyrics.
  for i in range(2):
    bounce(ball, 6, 24)

  lyrics.setText("Hap - py   Birth - Day    Dear   %s" % (enteredText))
  bounce(ball, 7, 28)

  lyrics.setText("Hap - py Birth-day   To   You")
  bounce(ball, 6, 24)

  message = Text(Point(midhoriz, WINDOW_HEIGHT - 75), "HAPPY!!!")
  message.setSize(36)

  lyrics.undraw()
  ball.undraw()

  # Induce seizure
  for i in range(100):
    win.setBackground("Lawn Green")
    message.setText("HAPPY!!!")
    message.draw(win)
    message.undraw()
    cake.move(10, 10)
    win.setBackground("Deep Pink")
    message.setText("BIRTHDAY!!!")
    message.draw(win)
    message.undraw()
    cake.move(-10, -10)
    time.sleep(.01)

  message.setText("HAPPY BIRTHDAY!!!")
  message.draw(win)

  # Exit the program.
  win.getMouse()
  win.close()

main()
