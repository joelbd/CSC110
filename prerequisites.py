# prerequisites.py
# joelDay

def checkPrerequisite(gradesData):
  if gradesData[4] == "Yes" or gradesData[2] == "Yes" and gradesData[3] == "Yes":
    results = "Prequisites met."
  else:
    results = "Prequisites not met."
  return results


def main():
  # studentData = getInput()
  studentData = ["Joel", "Day", "No", "No", "Yes"]
  status = checkPrerequisite(studentData)
  print(status)
  # outputResults(studentData, status)

main()
