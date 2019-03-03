import os
import csv

#format as percentage
def format_percentage(num):
    return str(num*100)[:4 + (2)] + '%'

voter_id=[]
candidates=[]
total_votes=0
candidate_list=[]


csvpath = os.path.join('election_data.csv')
 
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #print(csvreader)
    csv_header = next(csvreader)
    

    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        voter_id.append(row[0])
        candidates.append(row[2])

        total_votes += 1
        
    candidate_list=set(candidates)
    votes_per_candidate=dict()

    for name in candidate_list:
        votes_per_candidate[name] = 0

    votes = zip(voter_id, candidates)

    for voter_id, candidates in votes:
        if candidates in votes_per_candidate:
            votes_per_candidate[candidates] += 1

print(votes_per_candidate[name])
winner = max(votes_per_candidate, key=lambda k: votes_per_candidate[k])
#print(winner)
#print(votes_per_candidate)

print("Election Results")
print("_____________________________________")
print("Total Votes: " + str(total_votes))
print("_____________________________________")
for key, value in votes_per_candidate.items():
    print(key + ": " + str(round(((value/total_votes)*100),2)) + "% (" + str(value) + ")")
print("_____________________________________")
print ("Winner : " + winner)
print("_____________________________________")

path = os.path.join("output.txt")


with open(path, "w", newline='') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("_____________________________________\n")
    txtfile.write("Total Votes: " + str(total_votes)+ "\n")
    txtfile.write("_____________________________________\n")
    for key, value in votes_per_candidate.items():
        txtfile.write(key + ": " + str(round(((value/total_votes)*100),2)) + "% (" + str(value) + ") \n")
    txtfile.write("_____________________________________\n")
    txtfile.write("Winner : " + winner + "\n")
    txtfile.write("_____________________________________\n")



#------------------NOTES BELOW-----------------
       
#https://stackoverflow.com/questions/3561691/python-syntaxerror-eol-while-scanning-string-literal


   
    #find number of votes cast, count number of rows 


    #find complete list of candidates who received votes

    #print (winner)
    


###___________________________-

#import os
#import csv


#csvpath = os.path.join('election_data.csv')
 
#with open(csvpath, newline='') as csvfile:

    #csvreader = csv.reader(csvfile, delimiter=',')
    #data=pd.read_csv("election_data.csv")
    #df = pd.DataFrame(data)
    #print(csvreader)

    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

   
    #find number of votes cast, count number of rows 

    #total_votes=df.shape[0]

    #format as percentage
    #def format_percentage(num):
        #return str(num*100)[:4 + (2)] + '%'

    #find complete list of candidates who received votes
    #candidates = []
   
    #for x in df['Candidate']:
        #if x not in candidates:
            #candidates.append(x)

    
    #results = dict()
    #for x in df['Candidate']:
        #results[x] = results.get(x, 0) + 1
    

    #votes=list(results.values())
    #winner = max(votes)
    #print (winner)
    

    #print ("Election Results")
    #print ("-----------------------")
    #print ("Total Votes: " + str(total_votes))
    #print ("-----------------------")
    #for key, value in results.items():
        #print (str(key) + ": " + str(format_percentage(int(value)/total_votes)) + " (" + str(value) + ")")
    #print ("-----------------------")
    #for key, value in results.items():
        #if value == winner:
            #print ("Winner: " + str(key))
    #print ("-----------------------")

