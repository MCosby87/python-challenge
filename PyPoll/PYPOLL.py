import csv

inputfile='/Users/mario/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv'
outputfile='/Users/mario/python-challenge/PyPoll/pypoll.text'

polls=[]
polls_1={}
summary_1={}

with open(inputfile, newline='') as csvfile:
    pollreader=csv.reader(csvfile,delimiter=',')
    next(pollreader)
    text_file=open(outputfile,"w")
    text_file.write("Election Results")
    print("Election Results")
    text_file.write("\n-------------------------")
    print("-------------------------") 

    for line in pollreader:
        polls.append(line)
  
    text_file.write("\nTotal Votes: "+str(len(polls)))
    print("Total Votes: "+str(len(polls)))

    text_file.write("\n-------------------------")
    print("-------------------------")

    for line in polls:
        name_key=line[2]
        if name_key not in polls_1:
            polls_1[name_key]=0 
        polls_1[name_key]+=1
    
    total_polls=len(polls)
    for name in polls_1:
        summary_1[name]=round((polls_1[name]/total_polls)*100)
        text_file.write("\n"+str(name)+": "+str(summary_1[name])+"% "+"("+str(polls_1[name])+")")  
        print(str(name)+": "+str(summary_1[name])+"% "+"("+str(polls_1[name])+")")

    highest=0

    for name in summary_1:
        if highest < summary_1[name]:
            highest=summary_1[name]
            winner=name
            

    text_file.write("\n-------------------------")
    print("-------------------------")

    text_file.write("\nWinner: "+winner)
    print("Winner: "+winner)

    text_file.write("\n-------------------------")
    print("-------------------------")
    

text_file.close()