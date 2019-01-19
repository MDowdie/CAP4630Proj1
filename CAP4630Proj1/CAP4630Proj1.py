from State import State
import csv

# States.csv import
ListOfStates = []
with open('States.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
        ListOfStates.append( State(record["State"], record["Capital"], record["Abbreviation"], int(record["Population"]), record["Region"], int(record["US House Seats"])) )
print str(len(ListOfStates)) + " States Imported"



#Menu loop

#Menu option 1 - Print out a report on all states
def StateReport(ListOfStates):
    #1a - create report headers, determine column widths based on input data
    column_labels = ["State Name", "Capitol City", "State Abbr ", "State Population ", "Region", "US House Seats"]
    


#Menu option 2 - Sort list of states by state name (using Quick sort)

#Menu option 3 - Sort list of states by population (using Radix sort)


#Menu option 4 - Individual state report
#4a binary search, if current list order is state name ABC
#4b sequential search, if list order is not currently state name ABC


#Menu option 5 - quit