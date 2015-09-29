# fuelEconomy.py
# joelDay

# This program pulls data from two studies on fuel economy and outputs
# the average gas mileage and statistics for those vehicles

# Create tables to parse the files into
hwy = []
city = []
gasGuzzlersList = []

def readData(fileName):
  mpgData = open(fileName, "r")
  mpgList = [float(i) for i in mpgData.read().replace("\n", " ").split()]
  return mpgList

# Calculate the average mpg
def averageMPG(dataList):
  avgMPG = sum(dataList) / len(dataList)
  return avgMPG

# Enumerate and count vehicles meeting gas guzzler criteria
def countGasGuzzlers(masterList1, masterList2, threshold1, threshold2, targetList):
  for i in range(len(masterList1)):
    if masterList1[i] < threshold1:
      targetList.append(masterList1[i])
    elif masterList2[i] < threshold2:
      targetList.append(masterList2[i])
  return targetList

# Format and output the results of the study and this program
def printOutput(total, cAvg, hAvg, guzzlers):
  print(total, "cars were recently tested by the US Dept of Energy.")
  print("The average gas mileage found in the study was", cAvg, "for city and", hAvg, "for highway. \n")
  print("Of the vehicles tested,", guzzlers, "were considered gas guzzlers,")
  print("that is, less than 22 mpg in the city or 27 mpg on the highway.\n")
  print("For more information please visit: http://www.fueleconomy.gov")

# Execute the program
def main():
  city = readData("carModelData_city")
  hwy = readData("carModelData_hwy")
  cityAvg = averageMPG(city)
  hwyAvg = averageMPG(hwy)
  gasGuzzlers = countGasGuzzlers(city, hwy, 22.0, 27.0, gasGuzzlersList)
  printOutput(len(city), round(cityAvg, 1), round(hwyAvg, 1), len(gasGuzzlers))

main()
