# sphere.py
# joelDay

# This program takes an inputted radius and ouputs
# the surface area and volume.

from math import *

def getInput():

  # Intro program and prompt for a radius
  print("This program will calculate the surface and area")
  print("of a sphere given your inputted radius.")
  print()

  # Check for valid input
  while True:
    try:
      r = float(input("Please enter a radius: "))
      if r < 0:
        raise ValueError()
      break

    # Reject non numerical or negative values & start over
    except ValueError as exception:
      print("I'm sorry, please enter a valid radius.")
      print("For example: 4.25, or 8.")
      continue

    # Move on to the next steps
    else:
      break
  return r

def surfaceArea(r):
  sa = 4 * pi * r ** 2
  return sa

def volume(r):
  v = (4 / 3) * pi * r ** 3
  return v

def results(radius, area, volume):
  print()
  print("A sphere with radius %1.2f has a surface area of %1.2f" % (radius, area))
  print("and a volume of %1.2f." % (volume))

def main():

  radius = getInput()
  area = surfaceArea(radius)
  vol = volume(radius)
  results(radius, area, vol)

main()
