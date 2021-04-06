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
#Open csv
with open(csvpath, newline='') as electfile:
    csvreader = csv.reader(electfile, delimiter=',')
    csv_header = next(csvreader)

    for x in csvreader:
        voter_id.append(x[0])
        #Calculate the % of votes of each candidate
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
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    f"Khan: ({khan_votes})\n"
    f"Correy: ({correy_votes})\n"
    f"Li: ({li_votes})\n"
    f"O'Tooley: ({o_votes})\n"
    "-------------------------\n"
    "-------------------------\n")

#Print the analysis to the terminal
print(output)
#Export a text file with the results
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
