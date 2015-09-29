# file: acronym.py
# joelDay

# This program takes an entered phrase and creates then outputs
# an acronym in all capitals

def main():

  # Intro the program and prompt for input
  print("This program takes your phrase and makes it an acronym")
  print()
  phrase = input("Please enter your phrase here: ")

  # Split the phrase into a list
  wordList = phrase.split()

  # Create acronym variable
  acronym = ""

  # Define acronym's assets
  for word in wordList:
    acronym = acronym + word[0]

  # Output acronym in all caps
  print("The acronym is", acronym.upper(), end=".\n")

main()
