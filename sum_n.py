# File: ~/CSC110/sum_n.py
# joelDay
# The program lets the user select from two pre programmed summations or enter a
# user-defined number.

def main():
  print("Choose from the following:")
  print("a) The sum of numbers 1 - 10")
  print("b) The sum of numbers 1 - 100")
  print("c) Enter a custom number")
  selection = input("Make your selection: ")

  # If the user enters 'a' the summation of 1-10 will be calculated and printed
  if selection == 'a':
    num_input = 10

  # If the user enters 'b' the summation of 1-100 will be calculated and printed
  if selection == 'b':
    num_input = 100

  # If the user enters 'c' a prompt is given for the user to enter a natural number.
  if selection == 'c':
    num_input = eval(input("Please enter a natural number: "))

  # Compute the total of the naturals from 1 to num_input
  total = 1
  for i in range(num_input, 1, -1):
    total = total + i

  # Print the results
  print("The sum of the first", num_input, "naturals is", total)

main()
