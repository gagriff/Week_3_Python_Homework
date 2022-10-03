import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# initialize Totals dictionary
totalList = {'TotalMonths':0,
             'Total':0,
             'TotalChange':0,
             'MaxChange': ['',0],
             'MinChange': ['',0]}

# keep track of the previous Profit/Loss value to calculate change
vLastVal = ''

with open(csvpath, encoding='utf') as csvfile:

    csvread = csv.reader(csvfile,delimiter=',')

    csv_header = next(csvread)  # Skip Header Record

    for vRow in csvread:

        # increment Month count
        totalList['TotalMonths'] += 1

        # summarize Proit/Loss value over entire file
        vProfitLoss = int(vRow[1])
        totalList['Total'] += vProfitLoss

        if not vLastVal:
            vLastVal = vProfitLoss  # First record don't calculate change, record current value for next record
        else:
            # calculate change from previous month
            vChange = (vProfitLoss - vLastVal)
            # summarize the change over entire file
            totalList['TotalChange'] += vChange

            # record min / max change 
            if int(totalList['MaxChange'][1]) < (vProfitLoss - vLastVal):
                totalList['MaxChange'][0] = vRow[0]
                totalList['MaxChange'][1] = (vProfitLoss - vLastVal)

            if int(totalList['MinChange'][1]) > (vProfitLoss - vLastVal):
                totalList['MinChange'][0] = vRow[0]
                totalList['MinChange'][1] = (vProfitLoss - vLastVal)

            vLastVal = vProfitLoss


# Output to Screen and File in format
# Financial Analysis
# ----------------------------
# Total Months: nn
# Total: $nnn,nnn,nnn
# Average Change: $nnn,nnn,nnn.nn
# Greatest Increase in Profits: Month ($nnn,nnn,nnn)
# Greatest Decrease in Profits: Month ($nnn,nnn,nnn)


print("Financial Analysis")
print("----------------------------")
print(f"Total Months:   {totalList['TotalMonths']}")
print(f"Total:   ${totalList['Total']:,}")
print(f"Average Change:   ${round(totalList['TotalChange']/(totalList['TotalMonths']-1),2):,}")
print(f"Greatest Increase in Profits:   {totalList['MaxChange'][0]} (${int(totalList['MaxChange'][1]):,}) ")
print(f"Greatest Decrease in Profits:   {totalList['MinChange'][0]} (${int(totalList['MinChange'][1]):,}) ")

fileOutPath = 'budget_data_summary.txt'

fileOut = open(fileOutPath,'x')
fileOut.write("Financial Analysis\n")
fileOut.write("----------------------------\n")
fileOut.write(f"Total Months:   {totalList['TotalMonths']}\n")
fileOut.write(f"Total:   ${totalList['Total']:,}\n")
fileOut.write(f"Average Change:   ${round(totalList['TotalChange']/(totalList['TotalMonths']-1),2):,}\n")
fileOut.write(f"Greatest Increase in Profits:   {totalList['MaxChange'][0]} (${int(totalList['MaxChange'][1]):,})\n")
fileOut.write(f"Greatest Decrease in Profits:   {totalList['MinChange'][0]} (${int(totalList['MinChange'][1]):,})\n ")
fileOut.close()




