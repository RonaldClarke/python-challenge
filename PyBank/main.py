import csv
import os
filepath = os.path.join("/Users/ronaldclarke/Desktop/GitHub/python-challenge/PyBank/Resources/budget_data.csv")
MonthCount = 0
TotalProfLoss = 0
ProfitLoss = []
ChangeAm = []
date = []

with open(filepath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")   
    next(csvreader,None) #skips the header
    for row in csvreader:
        MonthCount = MonthCount + 1
        TotalProfLoss = TotalProfLoss + int(row[1])
        ProfitLoss.append(row[1])
        date.append(row[0])
    for i in range(1,len(ProfitLoss)):
        change = (float(ProfitLoss[i]) - float(ProfitLoss[i-1]))
        ChangeAm.append(change)
        avepl = (sum(ChangeAm)/len(ChangeAm))
        increase = max(ChangeAm)
        decrease = min(ChangeAm)
        increasedate = str(date[(ChangeAm.index(max(ChangeAm))+1)])
        decreasedate = str(date[ChangeAm.index(min(ChangeAm))+1])
print(avepl)
print(increase)
print(decrease)
print(TotalProfLoss)
print(MonthCount)
print(increasedate)
print(decreasedate)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(MonthCount))
print("Total: $" + str(TotalProfLoss))
print("Average Change: $" + str(round(avepl,2)))
print("Greatest Increase in Profits: " + increasedate + " ($" + str(round(increase)) + ")")
print("Greatest Decrease in Profits: " + decreasedate + " ($" + str(round(decrease)) + ")")

outputfile = os.path.join("/Users/ronaldclarke/Desktop/GitHub/python-challenge/PyBank/Analysis/results.txt")
with open (outputfile,"w") as resultsfile:
    resultsfile.write("Financial Analysis \n")
    resultsfile.write("---------------------------- \n")
    resultsfile.write("Total Months: " + str(MonthCount) + "\n")
    resultsfile.write("Total: $" + str(TotalProfLoss) + "\n")
    resultsfile.write("Average Change: $" + str(round(avepl,2)) + "\n")
    resultsfile.write("Greatest Increase in Profits: " + increasedate + " ($" + str(round(increase)) + ")\n")
    resultsfile.write("Greatest Decrease in Profits: " + decreasedate + " ($" + str(round(decrease)) + ")\n")