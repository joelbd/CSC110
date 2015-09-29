# batting_avg.py
# joelDay; calvinLe; samunSem; yaredShella

# This program orders and outputs the current batting average
# of the Seattle Mariner's starting lineup.

# Create list assets.
namesList = []
averages = []

def readFile():

  # Open and read the file into an ordered list.
  infile = open("MarinersBattingAverage.txt", "r")
  data = infile.read().replace("\n",", ").split(", ")
  return data

def createLists(dataList):

  # Create two ordered lists of names and batting averages.
  length = len(dataList)
  for i in range(1, length // 3 + 1):
    averages.append(dataList[3 * i - 1])
    namesList.append(dataList[3 * i - 2])
    namesList.append(dataList[3 * i - 3])

def printOutput():

  # Output statement with batting average.
  print("The Seattle Mariner's starting line up.")
  print()
  for i in range(len(averages)):
    print(namesList[2 * i], namesList[2 * i + 1], "is batting", averages[i], end=".\n")

def main():

  # Execute the program.
  stats = readFile()
  createLists(stats)
  printOutput()

main()
