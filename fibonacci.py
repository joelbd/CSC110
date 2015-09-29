# fibonacci.py
# joelDay

def getInput():
  numInput = eval(input("Please enter a natural number: "))
  return numInput

def getList(data):
  fib = [1]
  n = 0
  for i in range(data - 1):
    n = n + fib[i - 1]
    fib.append(n)
  return fib

def printOutput(count, dataList):
  print("The first", count, "characters of the Fibonacci sequence are:")
  print(dataList)

def repeat():
  response = input("Would you like to play again? Yes or No? ")
  while True:
    if response.lower() == "yes":
      main()
    else:
      break

def main():
  number = getInput()
  fibList = getList(number)
  printOutput(number, fibList)
  repeat()

main()
