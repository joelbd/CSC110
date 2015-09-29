# mastermind.py
# joelDay

# This program allows the user to play a game of Mastermind either
# with the accompanying mastermind_gui.py file or as a stand alone in the shell

from random import *
import math

# Create global mastermind attributes
class AbstractMasterMind:

  # Create color list and secret code.
  def __init__(self):
    self.colors = ["g", "b", "r", "y", "o", "p"]

    self.secretCode = []
    for i in range(4):
      self.secretCode.append(self.colors[randrange(len(self.colors))])

    self.roundNumber = 1

  def log(self, *message):
    raise NotImplementedError

  def readInput(self):
    raise NotImplementedError

  def writeOutput(self, *message):
    raise NotImplementedError

  # Challenge the current guess against the code for matches.
  def checkGuess(self, code, guess):
    match = 0
    close = 0
    tCode = list(code)
    tGuess = list(guess)

    for i in range(len(code)):
      if tGuess[i] == tCode[i]:
        match += 1
        tCode[i] = "Black"
        tGuess[i] = "consumed"

    for i in range(len(code)):
      try:
        found = tCode.index(tGuess[i])
        close += 1
        tCode[found] = "White"
      except ValueError:
        pass

    return match, close

  # Handle input and output and win/lose scenarios.
  def playRound(self):
    guess = self.readInput()
    secretCode = self.secretCode
    self.lastMatch, self.lastClose = self.checkGuess(self.secretCode, guess)
    if self.lastMatch == 4:
      self.writeOutput("You win!")
      return True
    elif self.roundNumber > 6:
      self.writeOutput("Oh Noes!!! You done lost! The answer was:", self.secretCode)
      return False
    else:
      self.writeOutput("Your guess has", self.lastMatch, "right and", self.lastClose, "close.")
      self.roundNumber += 1
      # return True

  def getRoundNumber(self):
    return self.roundNumber

  def getMatch(self):
    return self.lastMatch

  def getClose(self):
    return self.lastClose

# Terminal Variant
class TerminalMasterMind(AbstractMasterMind):

  def log(self, *message):
    self.writeOutput(*message)

  def readInput(self):
    guess = input("Please enter your four colors with commas: ").lower().replace(" ", "").split(",")
    return guess

  def writeOutput(self, *message):
    print(*message)

  def play(self):
    self.writeOutput("Welcome to Mastermind!  Guess the code with 4 colors (comma-separated):")
    self.writeOutput("g=green, b=blue, r=red, y=yellow, o=orange, p=purple")
    while True:
      shouldExit = self.playRound()
      if shouldExit:
        break

# Graphical Variant for the GUI
class GraphicalMasterMind(AbstractMasterMind):

  def log(self, *message):
    print(*message)

  # Set base parameters.
  def __init__(self):
    super().__init__()
    self.guessList = ["", "", "", ""]
    self.currentColor = ""

  def playRound(self):
    shouldExit = super().playRound()
    self.guessList = ["", "", "", ""]
    return shouldExit

  # Reject incomplete attempts for checkGuess().
  def confirmGuessLength(self):
    if "" in self.guessList:
      return False
    else:
      return True

  def getGuessList(self):
    return self.guessList

  def modifyCurrentGuess(self, guessIndex):
    self.guessList[guessIndex] = self.currentColor
    # self.log("this is the guess:", self.currentColor)

    return self.guessList

  def getCurrentColor(self):
    return self.currentColor

  def setCurrentColor(self, color):
    self.currentColor = color

  def readInput(self):
    return self.guessList

  def writeOutput(self, *message):
    print(*message)
    pass

# Test Variant for testing. To test a particular scenario, uncomment
# out the function call.
class FixtureMasterMind(AbstractMasterMind):

  def __init__(self, secretCode, guess, roundNumber):
    super().__init__()
    self.capturedOutput = []
    self.secretCode = secretCode
    self.cannedInput = guess
    self.roundNumber = roundNumber

  def log(self, *message):
    print(*message)

  def readInput(self):
    return self.cannedInput

  def writeOutput(self, *message):
    # self.log(*message)
    self.capturedOutput.append(message)

# game = TerminalMasterMind()
# game.play()

# checkGuess tests

def testCheckGuess(guess, secretCode, expectedMatch, expectedClose):
  game = FixtureMasterMind(secretCode, guess, 1)
  actualMatch, actualClose = game.checkGuess(secretCode, guess)
  if actualMatch == expectedMatch and actualClose == expectedClose:
    print("ok")
  else:
    print("FAIL: expected", expectedMatch, expectedClose, "but got", actualMatch, actualClose)

def itGetsOneCloseMatch():
  guess = ["r", "r", "r", "p"]
  secretCode = ["b", "b", "p", "b"]
  expectedMatch = 0
  expectedClose = 1
  testCheckGuess(guess, secretCode, expectedMatch, expectedClose)

# itGetsOneCloseMatch()

def itGetsTwoCloseMatches():
  guess = ["b", "r", "y", "p"]
  secretCode = ["r", "b", "o", "b"]
  expectedMatch = 0
  expectedClose = 2
  testCheckGuess(guess, secretCode, expectedMatch, expectedClose)

# itGetsTwoCloseMatches()

def itGetsOneCloseMatchesButHasThreeCopies():
  guess = ["b", "b", "b", "r"]
  secretCode = ["o", "o", "o", "b"]
  expectedMatch = 0
  expectedClose = 1
  testCheckGuess(guess, secretCode, expectedMatch, expectedClose)

# itGetsOneCloseMatchesButHasThreeCopies()

def itGetsOneExactMatch():
  guess = ["r", "y", "y", "p"]
  secretCode = ["r", "b", "o", "b"]
  expectedMatch = 1
  expectedClose = 0
  testCheckGuess(guess, secretCode, expectedMatch, expectedClose)

# itGetsOneExactMatch()

def itGetsOneExactMatchTwice():
  guess = ["r", "y", "y", "p"]
  secretCode = ["r", "b", "o", "b"]
  expectedMatch = 1
  expectedClose = 0
  testCheckGuess(guess, secretCode, expectedMatch, expectedClose)
  testCheckGuess(guess, secretCode, expectedMatch, expectedClose)

# itGetsOneExactMatchTwice()

def itGetsNoMatchesAndFourClose():
  guess = ["y", "o", "b", "r"]
  secretCode = ["r", "b", "o", "y"]
  expectedMatch = 0
  expectedClose = 4
  testCheckGuess(guess, secretCode, expectedMatch, expectedClose)

# itGetsNoMatchesAndFourClose()

# playRound tests

def testPlayRound(secretCode, guess, expectedShouldExit, roundNumber):
  game = FixtureMasterMind(secretCode, guess, roundNumber)
  actualShouldExit = game.playRound()
  if actualShouldExit == expectedShouldExit:
    print("ok")
  else:
    print("FAIL", actualShouldExit, expectedShouldExit)

def itWinsARound():
  secretCode = ["r", "r", "r", "r"]
  guess = ["r", "r", "r", "r"]
  expectedShouldExit = True
  testPlayRound(secretCode, guess, expectedShouldExit, 1)

# itWinsARound()

def itPlaysARound():
  secretCode = ["r", "r", "r", "r"]
  guess = ["r", "b", "o", "r"]
  expectedShouldExit = False
  testPlayRound(secretCode, guess, expectedShouldExit, 1)

# itPlaysARound()

def playSevenRounds():
    roundNumber = 7
    secretCode = ["r", "r", "r", "r"]
    guess = ["r", "b", "o", "r"]
    expectedShouldExit = True
    testPlayRound(secretCode, guess, expectedShouldExit, roundNumber)

# playSevenRounds()

def testForMatchDiscrepancy():
  roundNumber = 1
  secretCode = ['b', 'o', 'o', 'y']
  guess  = ["b", "o", "b", "y"]
  expectedClose = 0
  expectedMatch = 3
  testCheckGuess(guess, secretCode, expectedMatch, expectedClose)

# testForMatchDiscrepancy()

def testForFalseWhite():
  roundNumber = 1
  secretCode = ['b', 'b', 'r', 'o']
  guess  = ["b", "b", "b", "b"]
  expectedClose = 0
  expectedMatch = 2
  testCheckGuess(guess, secretCode, expectedMatch, expectedClose)

# testForFalseWhite()
