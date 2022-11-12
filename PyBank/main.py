#1) Define dependencies
#First we'll import the os module which will allow us to create file paths across operating systems
import os

#We will also import the module for reading CSV files
import csv


#2) Retireve the csv file we will use to generate our output file
#Map the path to the csv file 
budget_csv = os.path.join("PyBank",'Resources', 'budget_data.csv')

# Before opening the csv file, set up blank lists in which you will store values for the output file
# https://www.youtube.com/watch?v=bJDZ1wNKGEw
month_year = []   #will include the month-year where profits and losses were recorded
profits_loses = []  #will inlcude the profits/losses over those months
profit_changes = []   #the change in profits from one month to the next

#3)Read the data using the CSV module and generate content for your output file
with open(budget_csv) as csvfile:

    #CSV reader specifies a delimiter and variable that holds the contents of the file
    csvreader = csv.reader(csvfile, delimiter=',')

    #Print the csv reader path
    print(csvreader)

    #Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row of data after the header using a for loop that reads through each row of the data
    for row in csvreader:
        # print(row)    # toggle "commonet mode" on/off to view the data in the table (verification)

        month_year.append(row[0])  #copy data from the csv file to (month-year is in column 1, therefore, column index 0)
        profits_loses.append(int(row[1]))    #copy data from the csv file to the blank list created above (profits/losses in column 2, therefore, column index 1)
                                             #you have to specify it as an integer, or else will read it as string & result in errors later!!
                                             #https://bobbyhadz.com/blog/python-typeerror-can-only-concatenate-str-not-int-to-str

    # to check if the lists are complete, toggle the "print" functions below from "comment" mode
    # print(month_year)
    # print(len(month_year))    # Total # of months (toggle "comment mode" on/off to view the result) (verification)
    # print(profits_loses)
    # print(sum(profits_loses)) # Total amount of profits/losses) (toggle "comment mode" on/off to view the result) (verification)
   
    #To populate/append the "profits_changes" list, we will calculate the difference between each month 
    for index in range(len(profits_loses)-1):    #"for index in range(len(a_list)):" is a recommended for working with indexes
                                                 #https://www.adamsmith.haus/python/answers/how-to-use-range(len())-in-python
                                                 #after getting "list index out of range" error, I realized the issue was related with
                                                 #using the last index. The addition "-1" resolved the issue. 
                                                 ##https://www.freecodecamp.org/news/list-index-out-of-range-python-error-message-solved/
        # print(index)      # toggle "comment mode" on/off to view the index (verification)
        profit_changes.append(profits_loses[index+1] - profits_loses[index])
        
    # print(profit_changes)  # toggle "comment mode" on/off to view the results (verification)
    # print(round(sum(profit_changes)/len(profit_changes),2))   # Average change for all profits/losses (toggle "commonet mode" on/off to view the results) (verification)

    greatest_increase = max(profit_changes)     #instructs to find the max increase from one month to another
    greatest_increase_month = profit_changes.index(max(profit_changes))+1   #The month where the greates increase occurred is at "index+1"
    greatest_decrease = min(profit_changes)     #instructs to find the max increase from one month to another
    greatest_decrease_month = profit_changes.index(min(profit_changes))+1   #The month where the greates decrease occurred is at "index+1"
    # print(greatest_increase)        # toggle "comment mode" on/off to view the result (verification)
    # print(greatest_decrease)        # toggle "comment mode" on/off to view the result (verification)
    # print(month_year[greatest_increase_month])    # toggle "comment mode" on/off to view the result (verification)
    # print(month_year[greatest_decrease_month])    # toggle "comment mode" on/off to view the result (verification)

#4)Write the results to a text file
output_path = os.path.join("PyBank",'Analysis', 'Financial_Analysis.txt')

#\n is the same as hitting return on your keyboard (otherwise it will write in one continuous sentence)
with open (output_path,'w') as textfile:
    textfile.write("Financial Analysis" + '\n')  
    textfile.write("-----------------------------------------------------" + '\n')
    textfile.write(f"Total Months: {len(month_year)}" + '\n')
    textfile.write(f"Total Profits/Losses: ${sum(profits_loses)}" +'\n')
    textfile.write(f"Average Change (Profits/Losses): ${round(sum(profit_changes)/len(profit_changes),2)}" +'\n')
    textfile.write(f"Greatest Increase in Profit: {month_year[greatest_increase_month]} (${greatest_increase})" +'\n')
    textfile.write(f"Greatest Decrease in Profit: {month_year[greatest_decrease_month]} (${greatest_decrease})" +'\n')
