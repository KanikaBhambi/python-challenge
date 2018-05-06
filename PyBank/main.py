# importing the modules
import os
import csv

# Deleting Result.txt from previous code execution (if exists)
if os.path.exists("Result.txt"):
    os.remove("Result.txt")

# Defining function
def Budget(csvpath):
# Making empty lists for Revenue, Date and Rev_change
    Revenue = []
    Date = []
    Rev_change = []
    
# Reading budget_data_1.csv file
    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

# Using next to skip first title row in csv file
        next(csvreader) 

# Each row is read as a row for budget_data_1
        for row in csvreader:            
            Revenue.append(float(row[1]))
            Date.append(row[0])

        print("-----------------------------------")
        print("Financial Analysis")
        print("-----------------------------------")
        print("Total Months:", len(Date))
        print("Total Revenue: $", sum(Revenue))

# Looping through difference between all row of column 
# "Revenue" and calculating "Total Revenue Change" 
        for i in range(1,len(Revenue)):
            Rev_change.append(Revenue[i] - Revenue[i-1]) 
            
# Calculating Average Revenue change
# Calculating Max Revenue change and Min Revenue change
        Avg_rev_change = sum(Rev_change)/len(Rev_change)
        Max_rev_change = max(Rev_change)
        Min_rev_change = min(Rev_change)

        Max_rev_change_date = str(Date[Rev_change.index(max(Rev_change))])
        Min_rev_change_date = str(Date[Rev_change.index(min(Rev_change))])


        print("Average Revenue Change: $", round(Avg_rev_change))
        print("Greatest Increase in Revenue:", Max_rev_change_date,"($", Max_rev_change,")")
        print("Greatest Decrease in Revenue:", Min_rev_change_date,"($", Min_rev_change,")")
# Exporting results to a text file
        file = open('Result.txt','a')
        file.write("-----------------------------------\n")
        file.write('Financial Analysis for ' + csvpath + '\n')
        file.write("-----------------------------------\n")
        file.write("Total Months:"+ str(len(Date))+'\n')
        file.write('Total Revenue: $'+ str(sum(Revenue))+'\n')
        file.write('Average Revenue Change: $'+ str(round(Avg_rev_change))+'\n')
        file.write("Greatest Increase in Revenue:"+ str(Max_rev_change_date)+"($"+str(Max_rev_change)+")"+'\n')
        file.write("Greatest Decrease in Revenue:"+str(Min_rev_change_date)+"($"+ str(Min_rev_change)+")"+"\n")
        file.close()
# setting the path for sheet budget_data_1.csv
Budget_data_one_csvpath = os.path.join('Resources','budget_data_1.csv')
# Calling function
Budget(Budget_data_one_csvpath)

# setting the path for sheet budget_data_2.csv
Budget_data_two_csvpath = os.path.join('Resources','budget_data_2.csv')
# Calling function
Budget(Budget_data_two_csvpath)