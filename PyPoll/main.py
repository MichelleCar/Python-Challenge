#1) Define dependencies
#First we'll import the os module which will allow us to create file paths across operating systems
import os

#We will also import the module for reading CSV files
import csv

#2) Retireve the csv file we will use to generate our output file
#Map the path to the csv file 
poll_csv = os.path.join("PyPoll",'Resources', 'election_data.csv')

# Before opening the csv file, set up blank lists in which you will store values 
candidate_name = []   #this list will be populated by the csv data file
candidate_votes = []  #this list will hold the total votes for each candidate
percentage_votes = [] #this list will hold the percentage of votes for each candidate

#just as with any running tally, you need a starting point
total_votes = 0

# #3)Read the data using the CSV module and generate content for your output file
with open(poll_csv) as csvfile:

    #CSV reader specifies a delimiter and variable that holds the contents of the file
    csvreader = csv.reader(csvfile, delimiter=',')

    # #Print the csv reader path
    # print(csvreader) #toggle on/off to verify

    #Read the header row first 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #Read each row of data after the header using a for loop that reads through each row of the data
    for row in csvreader:
        # print(row)    # toggle "commonet mode" on/off to view the data in the table (verification)

        total_votes = total_votes + 1   #increases the TOTAL vote counter by 1 as it runs through the first row
                                        #Eachiteration will add additional votes for every entry in the csv
                                        #This was a better option than creating another list for the sole purpose of counting the # of rows
                                        #This is much more efficient
        if row[2] not in candidate_name:  #will add candidate's names to the empty list...candidate name is in the third column of the CSV (column index = 2)
            candidate_name.append(row[2]) #add candidate name to the list
            index = candidate_name.index(row[2])  #finds and returns the index of the element in the list
            candidate_votes.append(1) #add one vote to that candidate
        else:                                   #if the name already exists in the list
            index = candidate_name.index(row[2])    #finds the index of the candidate
            candidate_votes[index] = candidate_votes[index] + 1  #add another vote to the candidates votes

    #Once votes are tallied, calculate and add percentage for each candidate of the total vote
    for votes in candidate_votes: #will create a percentage of total votes for each candidate, aligning indexes
            percentage = ((votes/total_votes)*100) #calculate percentages ([candidate total votes ÷ total votes for all candidate] x 100)
            percentage = '%.3f' % percentage #formats percentage to 3 decimal places (https://stackoverflow.com/questions/51328193/understanding-the-print-format-3-in-python)
            percentage_votes.append(percentage) #add result to list

    #Gather final winning candidate
    winner = max(candidate_votes) #finds the maximum vote count by candidate
    index = candidate_votes.index(winner)   #finds the index of the candidate with the highest vote total
    winning_candidate = candidate_name[index]   #retrieves the index (essentially, the candidate name) that corresponds with the highest vote total
                                                #https://towardsdatascience.com/the-basics-of-indexing-and-slicing-python-lists-2d12c90a94cf 

# #verify your results # toggle "commonet mode" on/off to view the results
# print(total_votes)
# print('%.3f' % percentage) #format as % to 3 decimal places (https://www.adamsmith.haus/python/answers/how-to-format-a-number-as-a-percentage-in-python)
# print(candidates)
# print(winning_candidate)


# #4)Write the results to a text file
output_path = os.path.join('PyPoll','Analysis','Election_Results.txt')

#\n is the same as hitting return on your keyboard (otherwise it will write in one continuous sentence)
with open (output_path,'w') as textfile:
    textfile.write("Election Results" + '\n')  
    textfile.write("-----------------------------------------------------" + '\n')
    textfile.write(f"Total Votes: {total_votes}" + '\n')
    textfile.write("-----------------------------------------------------" + '\n')
    textfile.write("Individual Candidate Results" + '\n')
    for index in range(len(candidate_name)): #for loop to pull results for each candidate
        textfile.write(f"{candidate_name[index]}: {str(percentage_votes[index])}% ({str(candidate_votes[index])})" + '\n')
    textfile.write("-----------------------------------------------------" + '\n')     
    textfile.write(f"Winning Candidate: {winning_candidate}" +'\n')
    textfile.write("-----------------------------------------------------")     