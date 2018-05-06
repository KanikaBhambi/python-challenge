# importing all the modules
import os
import csv

Votes = []
Candidate = []
winner = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0

csvpath = os.path.join('Resources','election_data_1.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) 
    for row in csvreader:            
        Votes.append(row[2])
        if row[2] not in Candidate:
            Candidate.append(row[2])
            
        if row[2] == 'Vestal':
            count1 = count1 + 1
            
        elif row[2] == 'Torres':
            count2 = count2 + 1
            
        elif row[2] == 'Seth':
            count3 = count3 + 1
            
        else:
            count4 = count4 + 1

    winner.append(count1)
    winner.append(count2)
    winner.append(count3)
    winner.append(count4)
    
    
    Percentage1 = (count1/len(Votes))*100
    Percentage2 = (count2/len(Votes))*100
    Percentage3 = (count3/len(Votes))*100
    Percentage4 = (count4/len(Votes))*100

    candidate_one_result = Candidate[0] + ": " + str(Percentage1) + "%" + " (" + str(count1) + ")"
    candidate_two_result = Candidate[1] + ": " + str(Percentage2) + "%" + " (" + str(count2) + ")"
    candidate_three_result = Candidate[2] + ": " + str(Percentage3) + "%" + " (" + str(count3) + ")"
    candidate_four_result = Candidate[3] + ": " + str(Percentage4) + "%" + " (" + str(count4) + ")"
    total_votes = "Total Votes:" + str(len(Votes))
    election_winner = "Winner: " + Candidate[winner.index(max(winner))]
    print("Election Results")
    print("-----------------------------------")
    print(total_votes)
    print("-----------------------------------")
    print(candidate_one_result)
    print(candidate_two_result)
    print(candidate_three_result)
    print(candidate_four_result)
    print("-----------------------------------")
    print(election_winner)
    print("-----------------------------------")
    
# Exporting results to a text file
file = open('Result.txt','w')
file.write('Election Results \n')
file.write("-----------------------------------\n")
file.write(total_votes+'\n')
file.write("-----------------------------------\n")
file.write(candidate_one_result+'\n')
file.write(candidate_two_result+'\n')
file.write(candidate_three_result+'\n')
file.write(candidate_four_result+'\n')
file.write("-----------------------------------\n")
file.write(election_winner+'\n')
file.close()