import csv
import os
filepath = os.path.join("/Users/ronaldclarke/Desktop/GitHub/python-challenge/PyBank/Resources/budget_data.csv")
MonthCount = 0
TotalProfLoss = 0
ProfitLoss = []
ChangeAm = []

with open(filepath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")   
    next(csvreader,None) #skips the header
    for row in csvreader:
        MonthCount = MonthCount + 1
        TotalProfLoss = TotalProfLoss + int(row[1])
        ProfitLoss.append(row[1])
    for i in range(1,len(ProfitLoss)):
        change = (float(ProfitLoss[i]) - float(ProfitLoss[i-1]))
        ChangeAm.append(change)
        avepl = (sum(ChangeAm)/len(ChangeAm))
        increase = max(ChangeAm)
        decrease = min(ChangeAm)
print(avepl)
print(increase)
print(decrease)
print(TotalProfLoss)
print(MonthCount)

