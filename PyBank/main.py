import os
import csv


# set csv path
csvpath = os.path.join('Resources', 'budget_data.csv')
#open csv 


with open(csvpath) as csvfile:
    #set csv with , as delimiter
    csvread = csv.reader(csvfile, delimiter=',')
    
    
    #store header
    header_row = next(csvread)
    #store dates and profit data into list for later reference
    profits, dates = [],[]
    for row in csvread:
        profit = int(row[1])
        date = str(row[0])
        profits.append(profit)
        dates.append(date)
        #count months and total profits 
        totalprofits = sum(profits)
        months = len(profits)
    #calculate changes by report and store the new number into a new list for later analysis
    changes = []
    for x in range(1, 86):
        first = profits[x - 1]
        second = profits[x]
        change = second - first
        changes.append(change)
        #find max/min/average of the change list created in previous loop
        profitmax = max(changes)
        profitmin = min(changes)
        profitavg = round(sum(changes) / len(changes), 2)
        #index max/min positions in change list, add 1 to realign to date list. 
        indexmax = changes.index(profitmax)
        indexmin = changes.index(profitmin)
        datemax = dates[indexmax + 1]
        datemin = dates[indexmin + 1]


#print to terminal
print("Financial Analysis")
print('...................')
print(f"Total Months: {months}")
print(f"Total: ${totalprofits}")
print(f"Average Change: ${profitavg}")
print(f"Greatest Increase in Profit: {datemax} ${profitmax}")
print(f"Greatest Decrease in Profit: {datemin} ${profitmin}")
#create out going csv file.
outpath = os.path.join("Analysis", "Analysis.csv")

with open(outpath, 'w') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['.......................'])
    csvwriter.writerow([f'Total Months: {months}'])
    csvwriter.writerow([f'Total:${totalprofits}'])
    csvwriter.writerow([f'Average Change: ${profitavg}'])
    csvwriter.writerow([f'Greatest Increase in Profit: {datemax} ${profitmax}'])
    csvwriter.writerow([f'Greatest Decrease in Profit: {datemin} ${profitmin}'])


    