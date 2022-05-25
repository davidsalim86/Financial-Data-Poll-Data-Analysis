import os
import csv

#path for data
budget_csv = os.path.join("Resources","budget_data.csv")

#create empty lists
monthly_pnl = []
month = []

#read csv file
with open (budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    #save data in month & monthly_pnl lists
    sum_total = 0
    for row in csvreader:
        monthly_pnl.append(row[1])
        month.append(row[0])
        #calculate total pnl
        sum_total += int(row[1])

#calculate and save monthly pnl change amount in monthly_change list
monthly_change = []
count2 = -1
count3 = 0
for i in monthly_pnl:
    if count2 < 84 and count3 < 85:
        count2 += 1
        count3 += 1
        change = (int(monthly_pnl [count3]) - int(monthly_pnl [count2]))
        monthly_change.append(change)

#calculation for total months, average change, greatest increase in profits and greatest decrease in profits  
month_count = len(month)
average_change = "{:.2f}".format((int(monthly_pnl[-1]) - int(monthly_pnl[0]))/(month_count - 1))
max_change = max(monthly_change)
min_change = min(monthly_change)                                       
max_month_index = monthly_change.index(max_change)+1
min_month_index = monthly_change.index(min_change)+1
max_month = month [max_month_index]
min_month = month [min_month_index]

#print on terminal
print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${sum_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

# Specify the file to write and open using write mode
output_path = os.path.join("Analysis", "Analysis.txt")
with open(output_path, 'w') as f:

    #write analysis in text file
    f.write("Financial Analysis\n")
    f.write(f"----------------------------\n")
    f.write("Total Months:" " " f"{month_count}\n")
    f.write("Total:" " " "$" F"{sum_total}\n")
    f.write("Average Change:" " " "$" f"{average_change}\n")
    f.write("Greatest Increase in Profits:" " " f"{max_month}" " " f"(" "$" f"{max_change}" f")\n")
    f.write("Greatest Decrease in Profits:" " " f"{min_month}" " " f"(" "$" f"{min_change}" f")\n")

