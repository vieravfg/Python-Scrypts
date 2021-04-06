# Dependencies
import os
import csv
#File to read to:
csvpath = os.path.join("Resources", "budget_data.csv")
#File to output
file_to_output = os.path.join("Analysis", "pybank_analysis.txt")
# Lists to store data
profit_losses = []
date = []
changes = []
#Open csv
with open(csvpath, newline='') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    csv_header = next(csvreader)
    # Loop through looking 
    for row in csvreader:
        profit_losses.append(int(row[1]))
        date.append(row[0])

    for x in range(1,len(profit_losses)):
        changes.append(profit_losses[x]-profit_losses[x-1])

    #Calculate the total 
    total_sum = sum(profit_losses)
    #Calculate total months
    total_months = len(date)
    #Calculate the average
    changes_sum = sum(changes)
    average_change = round((changes_sum)/ (int(len(changes))), 2)
    #Calculate the greatest increase in profits
    great_increase = int(max(changes))
    #Calculate the greatest decrease in profits
    great_decrease = int(min(changes))
    #Calculate the dates for greatest increase and decrease
    index_great = changes.index(great_increase) + 1
    index_min = changes.index(great_decrease) + 1 
    max_date = date[index_great]
    min_date = date[index_min]

output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    "Total: " + '${}'.format(total_sum) + "\n"
    "Average Change: " + '${}'.format(average_change) + "\n"
    "Greatest Increase in Profit: " + max_date + " (" + '${}'.format(great_increase) +")" + "\n"
    "Greatest Decrease in Profit: " + min_date + " (" + '${}'.format(great_decrease) +")")

#Print the analysis to the terminal and export a text file with the results.
print(output)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
