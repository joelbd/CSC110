#File: getslope.py
#This program determines the slope of a line given two points
#joelDay

def main():
	x1,y1=eval(input("Please enter the coordinates of the first point (eg. X,Y): "))
	x2,y2=eval(input("Please enter the coordinates of the second point (eg. X,Y): "))
	if (x2-x1)==0:
		print("The slope is undefined.")
	else: 
		  (x2-x1)!=0:
			slope=(y2-y1)/(x2-x1)
			print("The slope of the line is",slope,end=".\n")
  
main()	
