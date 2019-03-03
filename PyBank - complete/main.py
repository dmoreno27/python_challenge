import os
import csv



csvpath = os.path.join('budget_data.csv')

outputpath = "summary.txt"

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    months=[]
    revenue=[]
    row_count = 0
    for row in csvreader:
        months.append(row[0])
        revenue.append(row[1])
        row_count += 1

    def as_currency(amount):
        if amount >= 0:
            return '${:,.2f}'.format(amount)
        else:
            return '-${:,.2f}'.format(-amount)

    max_inc = revenue[0]
    max_dec = revenue[0]
    total_revenue=0

    #print(len(revenue))
    for row in range(len(revenue)):
        if revenue[row]>=max_inc:
            max_inc=revenue[row]
            max_inc_month=months[row]
            total_revenue += int(revenue[row])    
        elif revenue[row] < max_dec:
            max_dec=revenue[row]
            max_dec_month=months[row]
            total_revenue += int(revenue[row])  

    avg_change=as_currency(total_revenue/len(months))
    total_revenue=as_currency(total_revenue)

    #print(avg_change)

    #output = os.path.join('output.txt')
    #writefile = csv.writer(output)

def final_results():
    print ("   ")
    print ("Financial Analysis")
    print ("-------------------------------")
    print (f"Total Months: " + str(len(months)))
    print (f"Total: " + str(total_revenue))
    print (f"Average Change: " + str(avg_change))
    print (f"Greatest Increase in Profits: " + str(max_inc_month) + " " + str(max_inc))
    print (f"Greatest Decrease in Profits: "+ str(max_dec_month) + " " + str(max_dec))

#final_results=final_results()

output = os.path.join('output','output.txt')

with open('output', 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(len(months)) + '\n')
    writefile.writelines('Total Revenue: ' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: ' + str(avg_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + max_inc_month + ' ($' + str(max_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + max_dec_month + ' ($' + str(max_dec) + ')')








#-------below are notes for the solution using pandas
        
#print(f"CSV Header: {csv_header}")  
#find number of rows   
    #data=pd.read_csv("budget_data.csv")
    #df = pd.DataFrame(data)

#sum the profit/loss column

    #Total = as_currency(df['Profit/Losses'].sum())
    #print(Total)

#average change in profit/loss over entire period
    #df['change'] = df['Profit/Losses'].shift(-1)- df['Profit/Losses']
    #av_change = as_currency(df['change'].mean())
    #print (df['change'].mean())
        
#greatest increase in profits (date and amount)
    #index = df['change'].idxmax()
    #max_inc_month=df.loc[index + 1, 'Date']
    #max_inc= as_currency(df.loc[index, 'change'])
    #print(df.loc[index, 'change'])
    
#greatest decrease in losses (date and amount)
    #index1 = df['change'].idxmin()
    #max_dec_month=df.loc[index1 + 1, 'Date']
    #max_dec= as_currency(df.loc[index1, 'change'])

#final printing
    #def final_results():
    #    print ("   ")
    #    print ("Financial Analysis")
    #    print ("-------------------------------")
    #    print (f"Total Months: " + str(df.shape[0]))
    #    print (f"Total: " + str(Total))
    #   print (f"Average Change: " + str(av_change))
    #    print (f"Greatest Increase in Profits: " + str(max_inc_month) + " " + str(max_inc))
    #    print (f"Greatest Decrease in Profits: "+ str(max_dec_month) + " " + str(max_dec))

