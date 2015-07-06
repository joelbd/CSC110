#Square root functions
import math

def main():
	num_input=eval(input("Please enter a natural number: "))
	result=math.sqrt(num_input)
	print(result)

main()

#factorial if/else trials
def main():
  selection = input("Choose from the following:\na) The Factorial of 10. \nb) The Factorial of 100. \nc) Enter a custom number. \nMake your selection: ")

  if selection == 'a':
    fact = 1
    for factor in range(10, 1, -1):
      fact = fact * factor
    print("The Factorial of 10 is", fact)
  if selection == 'b':
    fact = 1
    for factor in range(1,100):
      fact = fact * factor
    print("The Factorial of 100 is", fact)
  if selection == 'c':
    num_input = eval(input("Please enter a natural number: "))
    fact = 1
    for factor in range(1, num_input):
      fac = fact * factor
    print("The Factorial of", num_input, "is", fact)


main()

