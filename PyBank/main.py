
import csv 
filepath= r"C:\Users\Zaid Al-Saffar\Desktop\UCDSAC201902DATA4\03-Python\Homework\Instruction\PyBank\Resources\budget_data.csv" 
with open(filepath, newline='') as filepathCSV: 
    path = csv.reader(filepathCSV, delimiter = ",") 
    header = next(path) 
    month = [] 
    profit =[] 
    change = []
    for row in path: 
        month.append (row[0]) 
        profit.append (int(row[1])) 
    for j in range (1,len(profit)):
        change.append(int(profit[j]-profit[j-1]))
        
    print("Total Months:" +" "+ str(len(month))) 
    print("Total:"+ " " + str(sum(profit)))
    print("Average Change:" + " " + str((sum(profit)/len(month))))
    print(f'Greatest increase in profits: {month[change.index(max(change))+1]} ${max(change)}')
    print(f'Greatest decrease in profits: {month[change.index(min(change))+1]} ${min(change)}')
   