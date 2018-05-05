# importing the modules
import os
import csv

Revenue = []
Date = []
Rev_change = []

# Defining function
def Budget(csvpath):
    
# Reading budget_data_1.csv file
    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

# Using next to skip first title row in csv file
# Making empty lists for Revenue, Date and Rev_change
        next(csvreader) 

# Each row is read as a row for budget_data_1
        for row in csvreader:            
            Revenue.append(float(row[1]))
            Date.append(row[0])


        print("Financial Analysis")
        print("-----------------------------------")
        print("Total Months:", len(Date))
        print("Total Revenue: $", sum(Revenue))

# Looping through difference between all row of column 
# "Revenue" and calculating "Total Revenue Change" 
        for i in range(1,len(Revenue)):
            Rev_change.append(Revenue[i] - Revenue[i-1]) 
           # print (Rev_change[i-1])
# Calculating Average Revenue change
# Calculating Max Revenue change and Min Revenue change
        Avg_rev_change = sum(Rev_change)/len(Rev_change)
        Max_rev_change = max(Rev_change)
        Min_rev_change = min(Rev_change)
        
        Max_rev_change_date = str(Date[Rev_change.index(max(Rev_change))])
        # Min_rev_change_date = str(Date[Rev_change.index(min(Rev_change))])


        print("Avereage Revenue Change: $", round(Avg_rev_change))
        print("Greatest Increase in Revenue:", Max_rev_change_date,"($", Max_rev_change,")")
        #print("Greatest Decrease in Revenue:", Min_rev_change_date,"($", Min_rev_change,")")

# setting the path for sheet budget_data_1.csv
Budget_data_csvpath = os.path.join('Resources','budget_data_1.csv')

# Calling function
Budget(Budget_data_csvpath)

# setting the path for sheet budget_data_2.csv
Budget_data_csvpath = os.path.join('Resources','budget_data_2.csv')

# Calling function
Budget(Budget_data_csvpath)