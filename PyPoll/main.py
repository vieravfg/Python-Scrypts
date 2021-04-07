# PyPoll Homework Solution

# Dependencies
import os
import csv

#File to read to:
csvpath = os.path.join("Resources", "election_data.csv")

#File to output
file_to_output = os.path.join("Analysis", "pypoll_analysis.txt")

#Lists to store data
khan_list = []
o_list = []
li_list = []
correy_list = []
voter_id = []

#Read the csv file
with open(csvpath, newline='') as electfile:
    csvreader = csv.reader(electfile, delimiter=',')
    #
    csv_header = next(csvreader)
    #Loop through the csv file
    for x in csvreader:
        voter_id.append(x[0])
        #Conditionals: Creates a list for each candidate
        #If the candidate's "name" is in the csvreader's row[2], create a "new list" with the rows.
        if "Khan" in x[2]:
            khan_list.append(x)
        if "Correy" in x[2]:
            correy_list.append(x)
        if "Li" in x[2]:
            li_list.append(x)
        if "O'Tooley" in x[2]:
            o_list.append(x)
        
    #Calculate the number of votes of each candidate
    khan_votes = len(khan_list)
    correy_votes = len(correy_list)
    li_votes = len(li_list)
    o_votes = len(o_list)

    #Calculate the total number of votes
    total_votes = len(voter_id)

    #Calculate the percentages of each candidate
    khan_percent = (int(khan_votes)/int(total_votes)) * 100
    correy_percent = (int(correy_votes)/int(total_votes)) * 100
    li_percent = (int(li_votes)/int(total_votes)) * 100
    o_percent = (int(o_votes)/int(total_votes)) * 100
    
    #Calculate most popular
    number_votes = [(khan_votes),(correy_votes),(li_votes),(o_votes)]
    max_vote = max(number_votes)
    #Conditionals: Defines who is the winner with the most votes
    if int(max_vote) == int(khan_votes):
        winner = "Khan"
    if int(max_vote) == int(correy_votes):
        winner = "Correy"
    if int(max_vote) == int(li_votes):
        winner == "Li"
    if int(max_vote) == int(o_votes):
        winner == "O'Tooley"
#Generate the pypoll analysis output
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    "Khan: " + '{:,.3f}%'.format(khan_percent) + f" ({khan_votes})\n"
    "Correy: " + '{:,.3f}%'.format(correy_percent) + f" ({correy_votes})\n"
    "Li: " + '{:,.3f}%'.format(li_percent) + f" ({li_votes})\n"
    "O'Tooley: " + '{:,.3f}%'.format(o_percent) + f" ({o_votes})\n"
    "-------------------------\n"
    f"Winner: {winner}\n" 
    "-------------------------\n")

#Print the analysis to the terminal
print(output)
#Export a text file with the results
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
   
