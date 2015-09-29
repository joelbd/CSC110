# file: grade_calculator.py
# joelDay; arjunCook; thomasPernorio

# This program prompts for three grades out of 100 and calculates the
# grade average. It then use that average to determine the final
# letter grade.

letterGrades = ["F", "D", "C", "B", "A"]

# Handle the input
def grades(promptText):
  while True:
    try:
      grade_input = float(input(promptText))
      if grade_input > 110:
        raise ValueError()
      if grade_input < 0:
        raise ValueError()
      break

    # Reject non numerical or negative values & start over
    except ValueError as exception:
      print("I'm sorry, please enter a valid grade.")
      continue

    # Move on to the next steps
    else:
      break
  return grade_input

def main():
  # Introduce the program
  print("This program will calculate your letter grade")
  print("based off three percentage grades.")
  print()

  # Prompt for the numerical grades
  gradeOne = grades("Please enter your first grade: ")
  gradeTwo = grades("Now your second: ")
  gradeThree = grades("And your third: ")

  # Calculate the average grade
  grade_average = (gradeOne + gradeTwo + gradeThree) // 3

  # Prepare letter grade ID for output
  output = int((grade_average - 50) // 10)

  # Handle outlayer grades
  if output < 0:
    output = 0
  if output > 4:
    output = 4

  # Output the letter grade statement
  print("Your average grade is ", grade_average, "% and your grade is ", letterGrades[output], sep="", end=".\n")

main()

