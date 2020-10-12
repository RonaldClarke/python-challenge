import csv
import os
filepath = os.path.join("/Users/ronaldclarke/Desktop/GitHub/python-challenge/PyBank/Resources/budget_data.csv")
MonthCount = 0
TotalProfLoss = 0
with open(filepath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")   
    next(csvreader,None) #skips the header
    for row in csvreader:
        MonthCount = MonthCount + 1
        TotalProfLoss = TotalProfLoss + int(row[1])


