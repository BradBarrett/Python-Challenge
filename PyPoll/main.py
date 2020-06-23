import os
import csv
# import CSV Poll Results
csvpath = os.path.join("Resources", "election_data.csv")
#open poll results
with open(csvpath) as csvfile:
    #define poll results file 
    csvread =csv.reader(csvfile, delimiter=',')
    #skip header
    header_row = next(csvread)

    #pull CSV poll data into a list
    vote_list =[]
    for row in csvread:
        vote = str(row[2])
        vote_list.append(vote)
        #number of votes 
        length = len(vote_list)
    #identify number of candidates in race and add them to a new list
    candidate_list = []
    for x in vote_list:
        if x not in candidate_list:
            candidate_list.append(x)
            #how many candidates? print(candidate_list) to see candidates
            lengths = len(candidate_list)
    #assign Candidates in list to variables
    can1, can2, can3, can4 = [candidate_list[i] for i in (0, 1, 2 ,3)]
    #count votes for each candidate(variable)
    can1_votes = vote_list.count(can1)
    can2_votes = vote_list.count(can2)
    can3_votes = vote_list.count(can3)
    can4_votes = vote_list.count(can4)
    # assign candidate vote counts to a corresponding list
    winnerlist = [can1_votes, can2_votes, can3_votes, can4_votes]
    #find largest number of votes
    votemax = max(winnerlist)
    #index position of winner 
    winnerindex = winnerlist.index(votemax)
    #call out winner from corresponding candidate list
    winner = candidate_list[winnerindex]

    
    #calculate %s 
    can1_per = round(can1_votes / length * 100, 2)
    can2_per = round(can2_votes / length * 100, 2)
    can3_per = round(can3_votes / length * 100, 2)
    can4_per = round(can4_votes / length * 100, 2)

#print to terminal 
print("Election Results")
print("....................")
print(f"Total Votes: {length}")
print("....................")
print(f"{can1}: {can1_per}% ({can1_votes})")
print(f"{can2}: {can2_per}% ({can2_votes})")
print(f"{can3}: {can3_per}% ({can3_votes})")
print(f"{can4}: {can4_per}% ({can4_votes})")
print("....................")
print(f"Winner: {winner}")
print("....................")
#print CSV
outpath = os.path.join("Analysis", "Analysis.csv")

with open(outpath, 'w') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['....................'])
    csvwriter.writerow([f'Total Votes: {length}'])
    csvwriter.writerow(['....................'])
    csvwriter.writerow([f'{can1}: {can1_per}% ({can1_votes})'])
    csvwriter.writerow([f'{can2}: {can2_per}% ({can2_votes})'])
    csvwriter.writerow([f'{can3}: {can3_per}% ({can3_votes})'])
    csvwriter.writerow([f'{can4}: {can4_per}% ({can4_votes})'])
    csvwriter.writerow(['....................'])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(['....................'])