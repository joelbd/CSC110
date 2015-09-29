# mastermind_gui.py
# joelDay

# This file calls and provides assets for a GUI version of the Mastermind game
# controlled by mastermind.py.

import mastermind
from graphics import *
import math

WIN_WIDTH = 500
midhoriz = WIN_WIDTH // 2
WIN_HEIGHT = 800
midvert = WIN_HEIGHT // 2

# Create window and assets for game
def createWindow():
  win = GraphWin("Mastermind", WIN_WIDTH, WIN_HEIGHT)
  win.setCoords(0.0, 0.0, WIN_WIDTH, WIN_HEIGHT)
  win.setBackground("dim gray")

  bg = Image(Point(midhoriz, 0), "bg.gif")
  bg.draw(win)

  header = Text(Point(midhoriz-100, WIN_HEIGHT - 100), "Mastermind")
  header.setSize(46)
  header.setStyle("bold")
  header.setFill("white")
  header.draw(win)

  gradient = [
  "gray99", "gray95", "gray90", "gray85", "gray80",
  "gray75", "gray70", "gray65", "gray60", "gray55",
  "gray50", "gray45", "gray40", "gray35", "gray30",
  "gray25", "gray20", "gray15", "gray10", "gray5"
  ]

  for gray in gradient:
    header.move(5, -2.5)
    header.setFill(gray)
    time.sleep(.05)

  startButton = Rectangle(Point(midhoriz // 2, midvert), Point((midhoriz // 2) * 3, midvert - 100))
  startButton.setFill("White Smoke")
  startButton.setOutline("Dark Slate Gray")
  startButton.setWidth(10)
  startButton.draw(win)

  buttonText = Text(Point(midhoriz, midvert - 50), "Start a new game.")
  buttonText.setSize(23)
  buttonText.setFill("black")
  buttonText.draw(win)

  directions = Text(Point(midhoriz, WIN_HEIGHT - 250),
  "To play, simply pick a color from the \nsix options at the bottom and select the \nposition for which you want to guess that color.")
  directions.setSize(20)
  directions.setFill("black")
  directions.draw(win)

  directions2 = directions.clone()
  directions2.move(3,-3)
  directions2.setFill("yellow")
  directions2.draw(win)

  return win, bg, header, startButton, buttonText, directions, directions2

# Process the gameboard intro.
def clickThroughToGame(win, bg, header, startButton, buttonText, directions, directions2):
  while True:
    click = win.getMouse()
    x, y = click.getX(), click.getY()
    if (midhoriz // 2) <= x <= ((midhoriz // 2) * 3) and (midvert - 100) <= y <= midvert:
      break

  header.undraw()
  startButton.undraw()
  buttonText.undraw()
  directions.undraw()
  directions2.undraw()
  for i in range(160):
    bg.move(0, 5)
    time.sleep(.001)

# Call the graphical functions of mastermind.
def createGame(win, guessPegs, resultPegs):

  game = mastermind.GraphicalMasterMind()

  colors = {
    "": "SkyBlue1",
    "r": "red",
    "b": "blue",
    "g": "green",
    "p": "purple",
    "y": "yellow",
    "o": "orange"
  }

  # Handle all of the clicking actions.
  def onClick(point):

    # Put back into "world" reference frame
    x, y = win.toWorld(point.getX(), point.getY())

    if (WIN_WIDTH - 65) <= x <= (WIN_WIDTH - 20) and 25 <= y <= 75:
      win.close()

    if math.hypot(x - 75, y - 75) <= 20:
      game.setCurrentColor("r")
    if math.hypot(x - 25, y - 25) <= 20:
      game.setCurrentColor("b")
    if math.hypot(x - 175, y - 75) <= 20:
      game.setCurrentColor("g")
    if math.hypot(x - 125, y - 25) <= 20:
      game.setCurrentColor("p")
    if math.hypot(x - 275, y - 75) <= 20:
      game.setCurrentColor("y")
    if math.hypot(x - 225, y - 25) <= 20:
      game.setCurrentColor("o")

    for row in range(7):
      roundNumber = 7 - row

      if roundNumber != game.getRoundNumber():
        continue

      for column in range(4):
        if math.hypot(x - (50 + 100 * column), y - (WIN_HEIGHT - 50 -100 * row)) <= 25:
          game.modifyCurrentGuess(column)

          guessPegs[row][column].setFill(colors[game.getCurrentColor()])

    if (WIN_WIDTH - 175) <= x <= (WIN_WIDTH - 110) and 25 <= y <= 75:
      if game.confirmGuessLength():
        roundNumber = game.getRoundNumber()
        row = 7 - roundNumber
        shouldExit = game.playRound()
        match = game.getMatch()
        close = game.getClose()
        for i in range(match):
          resultPegs[row][i].setFill("black")
        for j in range(close):
          resultPegs[row][match + j].setFill("white")

      endBox = Rectangle(Point(midhoriz - 200, midvert + 110), Point(midhoriz + 200, midvert - 110))
      endBox.setFill("Violet Red")
      endBox.setOutline("Pale Violet Red")
      endBox.setWidth(15)

      # Endgame functions.
      if shouldExit == True:
        endBox.draw(win)
        winner = Text(Point(midhoriz, midvert), "Way to go, Ace!")
        winner.setFill("white")
        winner.setSize(36)
        winner.draw(win)
      if shouldExit == False:
        endBox.draw(win)
        lose = Text(Point(midhoriz, midvert), "Smooth move exlax! \nYou lost! \nThe answer was:\n %s" % (game.secretCode))
        lose.setStyle("bold")
        lose.setFill("white")
        lose.setSize(36)
        lose.draw(win)

  win.setMouseHandler(onClick)

# Draw the gameboard and set the IDs for the different pegs.
def gameLayout(win):

  stripe1 = Line(Point(-30, WIN_HEIGHT - 140), Point(130, WIN_HEIGHT + 30))
  stripe1.setWidth(50)
  stripe1.setFill("pink")
  stripe1.draw(win)

  stripe2 = Line(Point(-30, WIN_HEIGHT - 200), Point(190, WIN_HEIGHT + 30))
  stripe2.setWidth(15)
  stripe2.setFill("pink")
  stripe2.draw(win)

  stripe3 = Line(Point(-30, WIN_HEIGHT - 235), Point(225, WIN_HEIGHT + 30))
  stripe3.setWidth(15)
  stripe3.setFill("pink")
  stripe3.draw(win)

  guessPegs = []

  for i in range(7):
    guessPegs.append([])

    for n in range(4):
      circle = Circle(Point(50 + 100 * n, WIN_HEIGHT - 50 - 100 * i), 25)
      circle.setFill("SkyBlue1")
      circle.setOutline("sienna4")
      circle.setWidth(3)
      circle.draw(win)

      guessPegs[i].append(circle)

  resultPegs = []

  for row in range(7):
    resultPegs.append([])

    for j in range(2):
      smallCircleL = Circle(Point(WIN_WIDTH - 75, WIN_HEIGHT - 25 - 50 * j - 100 * row), 15)
      smallCircleL.setFill("SkyBlue1")
      smallCircleL.setOutline("sienna4")
      smallCircleL.setWidth(3)
      smallCircleL.draw(win)

      resultPegs[row].append(smallCircleL)

      smallCircleR = Circle(Point(WIN_WIDTH - 25, WIN_HEIGHT - 25 - 50 * j - 100 * row), 15)
      smallCircleR.setFill("SkyBlue1")
      smallCircleR.setOutline("sienna4")
      smallCircleR.setWidth(3)
      smallCircleR.draw(win)

      resultPegs[row].append(smallCircleR)

  redCircle = Circle(Point(75, 75), 20)
  redCircle.setFill("red")
  redCircle.setOutline("white")
  redCircle.draw(win)

  blueCircle = Circle(Point(25, 25), 20)
  blueCircle.setFill("blue")
  blueCircle.setOutline("white")
  blueCircle.draw(win)

  greenCircle = Circle(Point(175, 75), 20)
  greenCircle.setFill("green")
  greenCircle.setOutline("white")
  greenCircle.draw(win)

  purpleCircle = Circle(Point(125, 25), 20)
  purpleCircle.setFill("purple")
  purpleCircle.setOutline("white")
  purpleCircle.draw(win)

  yellowCircle = Circle(Point(275, 75), 20)
  yellowCircle.setFill("yellow")
  yellowCircle.setOutline("white")
  yellowCircle.draw(win)

  orangeCircle = Circle(Point(225, 25), 20)
  orangeCircle.setFill("orange")
  orangeCircle.setOutline("white")
  orangeCircle.draw(win)

  for i in range(7):
    dividers = Line(Point(WIN_WIDTH - 100, WIN_HEIGHT - 100 - 100 * i), Point(WIN_WIDTH, WIN_HEIGHT - 100 - 100 * i))
    dividers.setFill("light goldenrod")
    dividers.setWidth(3)
    dividers.draw(win)

  checkGuessButton = Rectangle(Point(WIN_WIDTH - 175, 75), Point(WIN_WIDTH - 110, 25))
  checkGuessButton.setFill("sienna4")
  checkGuessButton.setOutline("Saddle Brown")
  checkGuessButton.setWidth(10)
  checkGuessButton.draw(win)
  checkText = Text(Point(WIN_WIDTH - 140, 50), "Check ")
  checkText.setStyle("bold")
  checkText.setFill("white")
  checkText.setSize(16)
  checkText.draw(win)

  quitButton = checkGuessButton.clone()
  quitButton.move(90, 0)
  quitButton.draw(win)
  quitText = checkText.clone()
  quitText.move(90, 0)
  quitText.setText("Quit")
  quitText.draw(win)

  createGame(win, guessPegs, resultPegs)

def main():
  win, bg, header, startButton, buttonText, directions, directions2 = createWindow()
  clickThroughToGame(win, bg, header, startButton, buttonText, directions, directions2)
  gameLayout(win)

main()
