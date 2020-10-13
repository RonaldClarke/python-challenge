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

