#!/usr/bin/python
# File: area.py
# joelDay
# This program prompts the user for the lengths of the sides of a triangle
# then computes the area and outputs the final number.

# Importing the math module
import math

def main():
  print("Please enter the lengths of each side separated by a comma")
  num_input = input("eg. \"3,6,2\": ")
  a,b,c = num_input.split(",")
  a = float(a)
  b = float(b)
  c = float(c)
  # print(c)
  # print(type(c))
  float(a); float(b); float(c)
  s = (a + b + c) / 2
  area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
  print(area)

main()
