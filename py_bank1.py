#import librarires 
import os 
import csv

#print out the outcome - Financial Analysis, and a dotted line for readability 

print('Financial Analysis')
print('-----------------------------------------')

#tell python where to pull csv date from 
profit_data = os.path.join('budgetdata.csv')

#create lists to store the data we are going to analzy
months = []
profit = []
profit_change = []


#fill the lists with the data we are going to analyze
with open('budgetdata.csv', 'r') as budget:    #with this csv file
    csvreader = csv.reader(budget,delimiter=",") #seperated by rows

    header = next(csvreader) #skip the header 

    for row in csvreader: #for loop in our csv file
        months.append(row[0]) #list out the months in the first 0 indexed column 
        profit.append(int(row[1])) #list out the profit/losses in the second 0 indexed column

    for i in range(len(profit)-1): #for loop through the profit list, but less the first row - no change the first month 
        
        profit_change.append(profit[i+1]-profit[i]) #add the change in profit per month to the profit_change list by 
                                                    #subtracting the profit/loss by the previous month 

max_increase_value = max(profit_change) #find the max in the profit_change list and set it to a variable  
max_decrease_value = min(profit_change) #find the min in the profit_change list and set it to a variable 

max_increase_month = profit_change.index(max(profit_change)) + 1 #find which month the max increase landed on
max_decrease_month = profit_change.index(min(profit_change)) + 1 #find which month the min increase(or the max decrease) landed on

print(f"Total Months: {len(months)}") #print the count of months in the month list 
print(f"Total: ${sum(profit)}") #sum the profits in the profit list 
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}") #sum up the changes of profit in the profit change list &
                                                                            #average it by dividing by the count, round to dollars
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")  #print the month and max increase
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})") #print the month and max decrease
