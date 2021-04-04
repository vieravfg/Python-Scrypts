# Dependencies
import os
import csv
#file to read to:
csvpath = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")
print("----------------------------")

# Lists to store data
profit_losses = []
date = []

#Open cvs
with open(csvpath, newline='') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    csv_header = next(csvreader)
    # Loop through looking 
    for row in csvreader:
        profit_losses.append(int(row[1]))
        date.append(row[0])
    
    total_sum = sum(profit_losses)
    total_months = len(date)
        # average_change = round(int(total_sum)/ int(total_months), 2))

    print("Total Months: " + str(total_months))
    print("Total: " + '${}'.format(total_sum))

        #print("Average:" + str(average_change))
        #print("Greatest Increase in Profits:")
        #print("Greatest Decrease in Profits:")

#print the analysis to the terminal and export a text file with the results.
#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)
       
