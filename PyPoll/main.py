import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

# initialize candidate dictionary
candidateDict = {}

with open(csvpath, encoding='utf') as csvfile:

    csvread = csv.reader(csvfile,delimiter=',')

    csv_header = next(csvread)  # Skip Header Record

    for vRow in csvread:

        if vRow[2] not in candidateDict:
            candidateDict[vRow[2]] = 1
        else:
            candidateDict[vRow[2]] += 1

totalVotes = 0
topVote = 0

for i in candidateDict:
    totalVotes = totalVotes + candidateDict[i]

    if candidateDict[i] > topVote:
        winner = i
        topVote = candidateDict[i]

# Election Results
# -------------------------
# Total Votes: nnn,nnn,nnn
# -------------------------
# cancidate 1: nn.nn% (nnn,nnn,nnn)
# cancidate 2: nn.nn% (nnn,nnn,nnn)
# cancidate 3: nn.nn% (nnn,nnn,nnn)
# .....
# cancidate n: nn.nn% (nnn,nnn,nnn)
# -------------------------
# Winner: candidate
# -------------------------        

print("Election Results")
print("-------------------------")
print(f"Total Votes:    {totalVotes:,}")
print("-------------------------")

for j in candidateDict:
    print(f"{j}: {round(int(candidateDict[j])/totalVotes*100,3)}% ({candidateDict[j]:,})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

fileOutPath = 'election_data_summary.txt'
fileOut = open(fileOutPath,'x')

fileOut.write("Election Results\n")
fileOut.write("-------------------------\n")
fileOut.write(f"Total Votes:    {totalVotes:,}\n")
fileOut.write("-------------------------\n")

for j in candidateDict:
    fileOut.write(f"{j}: {round(int(candidateDict[j])/totalVotes*100,3)}% ({candidateDict[j]:,})\n")

fileOut.write("-------------------------\n")
fileOut.write(f"Winner: {winner}\n")
fileOut.write("-------------------------\n")

fileOut.close()
