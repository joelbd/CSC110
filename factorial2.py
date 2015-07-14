# File: factorial2.py
# joelDay

# This program requests a whole number, n, from the user and calculates
# outputs the n-factorial.
def main():

  print("The program will ask you to input a whole number, n")
  print("It will then calculate and output n-factorial")
  print()

  # Prompt the user to input a whole number.
  n = eval(input("Please enter a whole number: "))

  # Initializing the variable fact2 to equal 1.
  fact2 = 1

  # Calculating n-factorial (fact2) with a definite loop.
  for i in range(n, 1, -1):
    fact2 = fact2 * i

  # Output the result of n-factorial, fact2.
  print("The factorial of", n, "is", fact2, end=".\n")

main()
