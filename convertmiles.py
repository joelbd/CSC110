#	File: convertmiles.py
#	This program converts distance in miles to distance in kilometers
#	Day

def main():
	miles = eval(input("Enter the distance in miles:"))
	kilometers = miles * 1.60934
	print("The distance is:",kilometers,"km")

main()