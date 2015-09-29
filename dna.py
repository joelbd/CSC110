# dna.py
# joelDay

# This program takes an inputted file and converts it to two strings.
# It then searches the larger string for instances of the smaller
# substring and outputs the indices


def readFile():
  # Open and read the file into a list.
  infile = open("motifFinding.txt", "r")
  data = infile.read().replace("\n",", ").split(", ")
  s = data[0]
  t = data[1]
  return s, t

# Locate and record instances of the variable
def findVariable(dataSet1, dataSet2, targetList):
  n = 0
  for i in range(len(dataSet1)):
    if n != -1:
      n = dataSet1.find(dataSet2, n + 1)
      targetList.append(n)
    else:
      break
  return targetList

# Define and print output
def printOutput(sequence, originalSequence):
  print("The sequence was found %d times at the following indices: " % (len(sequence) - 1))
  for i in range(len(sequence) - 1):
    print(sequence[i],  end = " ")
  print()

def main():
  pos = []
  s, t = readFile()
  positions = findVariable(s, t, pos)
  printOutput(positions, s)

main()
