# Dependencies
import os
import csv
#file to read to:
csvpath = os.path.join("Resources", "budget_data.csv")
#file to output
file_to_output = os.path.join("Analysis", "pybank_analysis.txt")
# Lists to store data
profit_losses = []
date = []
changes = []

#Open cvs
with open(csvpath, newline='') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    csv_header = next(csvreader)
    # Loop through looking 
    for row in csvreader:
        profit_losses.append(int(row[1]))
        date.append(row[0])

    for x in range(1,len(profit_losses)):
        changes.append(profit_losses[x]-profit_losses[x-1])

    total_sum = sum(profit_losses)
    total_months = len(date)

    changes_sum = sum(changes)
    average_change = round((changes_sum)/ (int(len(changes))), 2)

output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    "Total: " + '${}'.format(total_sum) + "\n"
    "Average Change: " + '${}'.format(average_change))

        #print("Average:" + str(average_change))
        #print("Greatest Increase in Profits:")
        #print("Greatest Decrease in Profits:")

#print the analysis to the terminal and export a text file with the results.
print(output)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
  #  f"Approximate Word Count: {word_count}\n"
#with open(file_to_output, "a") as txt_file:
    #txt_file.write(output)
