# file: factorial.py
# joelDay

# This program prompts the user to enter a natural number (n)
# and outputs the nfactorial
def main():
  # num_input = eval(input("Please enter a natural number: "))
  # fact = 1
  # for factor in range(num_input, 1, -1):
  #   fact = fact * factor
  # print("The Factorial of", num_input, "is", fact)

  num_input = eval(input("Please enter a natural number: "))
  fact = num_input
  for factor in range(1, num_input):
    fact = fact * factor
  print("The factorial of", num_input, "is", fact)

main()
