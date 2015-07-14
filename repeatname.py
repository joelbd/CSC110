#File: repeatname.py
#joelDay

#This program requests the user's name and outputs it five number of times.
def main():
  name = input("Please give me your name: ")
  for i in range(5):
    print(name, end=".\n")
    # print("Your name is", name ,end = ".\n")

main()
