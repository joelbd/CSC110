# qt13.py
# joelDay

# This program prompts the user to enter either a number from 10 to 50
# or choose a random number. It then computes the min, max, & avg and
# outputs the results.

from random import *

# def getInput():
#   numbers = []
#   for i in range(randrange(10, 51)):
#     n = randrange(50, 100)
#     numbers.append(n)
#   return numbers

def getInput():
  numbers = []
  numInput = input("Please enter a number between 10 and 50 or press enter for a random length: ")

  # Deliver a randomized list if "enter" is pressed
  if numInput == "":
    for i in range(randrange(10, 51)):
      n = randrange(50, 100)
      numbers.append(n)

  # Reject any other non-conforming input and return the list
  else:
    while True:
      try:
        numInput = int(numInput)
        if numInput < 10 or numInput > 50:
            raise ValueError()
        else:
          for i in range(numInput):
            n = randrange(50, 100)
            numbers.append(n)
        break
      except ValueError:
        break

  if numbers !=  []:
    return numbers

def averageList(numList):
  avg = sum(numList) / len(numList)
  return avg

def findMaximum(dataList):
  maxNum = dataList[0]
  for i in range(len(dataList)):
    if dataList[i] > maxNum:
      maxNum = dataList[i]
  return maxNum

def findMinimum(dataList):
  minNum = dataList[0]
  for i in range(len(dataList)):
    if dataList[i] < minNum:
      minNum = dataList[i]
  return minNum

def outputResults(dataSet, avg, min, max):
  print(len(dataSet), "numbers were chosen at random.")
  print("Here are the numbers used:", (dataSet))
  print("\nThe highest number was", max, "and the lowest was", min, end = ".\n")
  print("The average of the entire set is", round(avg, 2), end = ".\n")

def main():
  try:
    numbersList = getInput()
    numAvg = averageList(numbersList)
    numMax = findMaximum(numbersList)
    numMin = findMinimum(numbersList)
    outputResults(numbersList, numAvg, numMin, numMax)
  except:
    print("\nI'm sorry that is an invalid entry.")

main()
