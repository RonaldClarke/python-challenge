import csv
import os
filepath = os.path.join("/Users/ronaldclarke/Desktop/GitHub/python-challenge/PyPoll/Resources/election_data.csv")

TotalVotes = 0
candidates = []
votecounts = []

with open (filepath, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        TotalVotes = TotalVotes + 1
        candidate = (row[2])
        if candidate in candidates:
            indexnum = candidates.index(candidate)
            votecounts[indexnum] = votecounts[indexnum] + 1
            
        else:
            candidates.append(row[2])
            votecounts.append(1)

print(votecounts)
print(candidates)

print("Election Results")
print("---------------------")
print("Total Votes: " + str(TotalVotes))
print("---------------------")
winnervote = 0
for candidate in candidates:
    print(candidates[candidates.index(candidate)] + ": " + str(round((((votecounts[candidates.index(candidate)])/TotalVotes)*100),3)) + "% (" + str(votecounts[candidates.index(candidate)]) + ")")
    if votecounts[candidates.index(candidate)] > winnervote:
        winnervote = votecounts[candidates.index(candidate)]
        winner = candidates[candidates.index(candidate)]
print("----------------------")
print("Winner: " + winner)
outputfile = os.path.join("/Users/ronaldclarke/Desktop/GitHub/python-challenge/PyPoll/Analysis/results.txt")
with open (outputfile,"w") as resultsfile:
    resultsfile.write("Results")