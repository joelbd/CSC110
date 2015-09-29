# file: days.py
# joelDay

# This program prompts the user for the numeric value of the day,
# with Sunday being day 1, and outputs the three letter abbr for that day

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def main():
  print("This program will give you the day of the week")
  print("Please enter a day of the week in number format")
  day_input = eval(input("(eg: Sunday = 1, Monday = 2, etc: "))

  output = days[day_input - 1]
  if day_input == 1:
    day_output = str(day_input) + "st"
  if day_input == 2:
    day_output = str(day_input) + "nd"
  if day_input == 3:
    day_output = str(day_input) + "rd"
  if day_input > 3:
    day_output = str(day_input) + "th"

  print("The",day_output, "day of the week is", (output), end=".\n")

main()
