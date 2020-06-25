#import csv
import csv

#import os
import os
#path to collect data from the resources folder
bank_csv = os.path.join('Resources', 'budget_data.csv')

#path to write data to the analysis folder
#results_csv = os.path.join('..', 'analysis', 'PyBankResults.txt')

months = 0
total = 0
maximum = 0
minimum = 0

#read in the csv file
with open(bank_csv, 'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header row
    next(csvreader)

    #loop through the data
    for row in csvreader:
        #count the number of months
        months = months + 1
        #add the profit/losses for each month
        total = total + int(row[1])

        #find the highest profit/loss value
        if int(maximum) < int(row[1]):
            maximum = row[1]
            highDay = row[0]
        #find the lowest profit/loss value
        elif int(minimum) > int(row[1]):
            minimum = row[1]
            lowDay = row[0]

    # print the number of months and the total profits/losses
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    #print the greatest increase and greatest decrease
    print(f'Greatest Increase in Profits: {highDay} (${maximum})')
    print(f'Greatest Decrease in Profits: {lowDay} (${minimum})')

    #output the results in a text file
    text_file = open('PyBankResults.txt', 'w')
    text_file.write(f'Total Months: {months}''\n')
    text_file.write(f'Total: ${total}''\n')
    text_file.write(f'Greatest Increase in Profits: {highDay} (${maximum})''\n')
    text_file.write(f'Greatest Decrease in Profits: {lowDay} (${minimum})')
    text_file.close



