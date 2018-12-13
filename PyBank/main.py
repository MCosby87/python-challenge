import os

import csv

csvpath = "/Users/mario/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"


with open(csvpath, "r") as csvfile:
  
    list_1 = []
    total = 0
    months = 0
    
    csvreader = csv.reader(csvfile, delimiter=',')
   
    header = next(csvreader)
   
    for row in csv.reader(csvfile):
        list_1.append(row[1])
        total = total + (int(row[1]))
        months = months + 1
        
        
print("Financial Analysis")
print("------------------------")
print("Total months: " + str(months))
print("Total volume: " + str(total))
        
with open(csvpath, "r") as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    list_2 = []
    for x, y in zip(list_1, list_1[1:]):

        list_2.append(int(x) - int(y))

        totalchange = sum(list_2)
        average = totalchange / months
print("Average monthly change: "+ str(average))

greatestincrease = max(list_2)
greatestdecrease = min(list_2)
print("Greatest increase: " + str(greatestincrease))
print("Greatest decrease: " + str(greatestdecrease))


text_file = open("PYBANK.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("------------------------\n")
text_file.write("Total months: " + str(months) + "\n")
text_file.write("Total volume: " + str(total) + "\n")
text_file.write("Average monthly change: " + str(average) + "\n")
text_file.write("Greatest increase: " + str(greatestincrease) + "\n")
text_file.write("Greatest decrease: " + str(greatestdecrease) + "\n")
text_file.close()