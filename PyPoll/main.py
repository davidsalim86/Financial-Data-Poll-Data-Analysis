import os
import csv

#path for data
poll_csv = os.path.join("Resources","election_data.csv")

#list to store data
candidatename = []

#read csv file
with open (poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    count = 0
    countcandidate1 = 0
    countcandidate2 = 0
    countcandidate3 = 0
    countcandidate4 = 0
    
    for row in csvreader:
        #add candidatename and create list of candidate
        candidatename.append(row[2])
        candidatename = list(dict.fromkeys(candidatename))
        
        #count total votes
        count += 1
        
        #count votes for each candidate
        if row[2] == candidatename [0]:
            countcandidate1 += 1
            percent1 = countcandidate1 / count
            percentformat1 = "{:.3%}".format(percent1)
        elif row[2] == candidatename [1]:
            countcandidate2 += 1
            percent2 = countcandidate2 / count
            percentformat2 = "{:.3%}".format(percent2)
        elif row [2] == candidatename [2]:
            countcandidate3 += 1
            percent3 = countcandidate3 / count
            percentformat3 = "{:.3%}".format(percent3)
        elif row [2] == candidatename [3]:
            countcandidate4 += 1  
            percent4 = countcandidate4 / count
            percentformat4 = "{:.3%}".format(percent4)
        
        #count max
        countcandidate = []
        countcandidate.append (countcandidate1)
        countcandidate.append (countcandidate2)
        countcandidate.append (countcandidate3)
        countcandidate.append (countcandidate4)
        max_count = max(countcandidate) 
        
        if max_count == countcandidate1:
            winner = candidatename[0]
        elif max_count == countcandidate2:
            winner = candidatename[1]
        elif max_count == countcandidate3:
            winner = candidatename[2]
        elif max_count == countcandidate4:
            winner = candidatename[3]
            
    #print analysis to terminal    
    print (f"Election Results")
    print (f"-------------------------")
    print (f"Total Votes: {count}")
    print (f"-------------------------")
    print (f"{candidatename [0]}: {percentformat1} ({countcandidate1})")
    print (f"{candidatename [1]}: {percentformat2} ({countcandidate2})")
    print (f"{candidatename [2]}: {percentformat3} ({countcandidate3})")
    print (f"{candidatename [3]}: {percentformat4} ({countcandidate4})")
    print (f"-------------------------")
    print (f"Winner: {winner}")
    print (f"-------------------------")
    
# Specify the file to write and open using write mode
output_path = os.path.join("Analysis", "Analysis.txt")
with open(output_path, "w") as f:
    
    #write analysis in a text file
    f.write("Election Results\n") 
    f.write("-------------------------\n")
    f.write("Total Votes:" " " f"{count}\n")
    f.write("-------------------------\n")
    f.write(f"{candidatename [0]}" ": " f"{percentformat1}" " " f"({countcandidate1})\n")
    f.write(f"{candidatename [1]}" ": " f"{percentformat2}" " " f"({countcandidate2})\n")
    f.write(f"{candidatename [2]}" ": " f"{percentformat3}" " " f"({countcandidate3})\n")
    f.write(f"{candidatename [3]}" ": " f"{percentformat4}" " " f"({countcandidate4})\n")
    f.write("-------------------------\n")
    f.write("Winner:" " " f"{winner}\n")
    f.write("-------------------------\n")
    