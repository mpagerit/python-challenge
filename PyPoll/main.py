#import csv
import csv

#import os
import os

#path to collect data from the resources folder
poll_csv = os.path.join('Resources', 'election_data.csv')

#path to write data to the analysis folder
poll_text = os.path.join('analysis', 'PyPollResults.txt')

#define the dictionary to be filled with candidates and their vote tallies
voteTallies = {}
totalVotes = 0
mostVotes = 0

#read in the csv file
with open(poll_csv, 'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #store the header row
    header = next(csvreader)

    #loop through the data
    for row in csvreader:
        #count the number of votes
        totalVotes = totalVotes + 1

        #check to see if a candidate is in the voteTally dictionary, update it accordingly
        if row[2] in voteTallies.keys():
             voteTallies[row[2]] += 1
        else:
             voteTallies[row[2]] = 1


    #find the candidate with the greatest number of votes
    for candidate in voteTallies:
        if voteTallies[candidate] > mostVotes:
            mostVotes = voteTallies[candidate]
            winner = candidate


#output results into a text file and print to the terminal
#output the results in a text  file
with open(poll_text, 'w') as text_file:
    #write to the text file
    text_file.write(f'Election Results''\n')
    text_file.write('------------------------------''\n')
    text_file.write(f'Total Votes: {totalVotes}''\n')
    text_file.write('------------------------------''\n')

    #print to the terminal
    print(f'Election Results')
    print('------------------------------')
    print(f'Total Votes: {totalVotes}')
    print('------------------------------')

    for candidate in voteTallies:
        #calculate the percentage of the vote received by the candidate
        percentVote = round((voteTallies[candidate] / totalVotes * 100), 3)
        
        #print the candidate's results
        print(f'{candidate}: {percentVote}% ({voteTallies[candidate]})')

        #write results to the text file
        text_file.write(f'{candidate}: {percentVote}% ({voteTallies[candidate]})''\n')

    #print the winner
    print('------------------------------')
    print(f'Winner: {winner}')
    print('------------------------------')

    #write the winner to the text file
    text_file.write('------------------------------''\n')
    text_file.write(f'Winner: {winner}''\n')
    text_file.write('------------------------------''\n')

