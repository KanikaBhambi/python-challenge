import csv
import os

newcsv =[]

csvpath = os.path.join('Resources','employee_data1.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# create individual list
  newcsv = "Emp ID":[], "First Name": [], "Last Name": [], "DOB": [], "SSN":[], "State":[]}
    next(csvreader)
    for row in csvreader:
        First = row[1].split()[0]
        Last = row[1].split()[1]
         newcsv["Emp ID"].append(row[0])
         newcsv["First Name"].append(First)
         newcsv["Last Name"].append(Last)
         newcsv["DOB"].append(row[2])
         newcsv["SSN"].append(row[3])
         newcsv["State"].append(row[4])
    print (newcsv)

output_path = os.path.join("Resources", "new.csv")
with open(output_path, 'w', newline='') as datafile:
    #fieldnames = ['Emp ID', 'First_Name', 'Last_Name','DOB','SSN','State'] 
    w = csv.writer(datafile)
    #w.writeheader()
    w.writerows(['Emp ID', 'First_Name', 'Last_Name','DOB','SSN','State'])
    # for row in fieldnames:
    #     w.writerows(newcsv)