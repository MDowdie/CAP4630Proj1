from State import State
import csv
import sys

# States.csv import
ListOfStates = []
with open('States.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
        ListOfStates.append( State(record["State"], record["Capital"], record["Abbreviation"], int(record["Population"]), record["Region"], int(record["US House Seats"])) )
print str(len(ListOfStates)) + " States Imported"



#Menu loop

#Menu option 1 - Print out a report on all states
def PrintStateReport(ListOfStates):
    #1a - create report headers; format: ["Header Title", Header Length]
    columns = [["State Name",len("State Name")], ["Capital City",len("Capital City")], ["State Abbr",len("State Abbr")], ["State Population",len("State Population")], ["Region",len("Region")], ["US House Seats",len("US House Seats")]]
    
    #1b - determine column widths based on input data
    for record in ListOfStates:
        columns[0][1] = max(columns[0][1],len(record.StateName))
        columns[1][1] = max(columns[1][1],len(record.CapitalCity))
        columns[2][1] = max(columns[2][1],len(record.Abbreviation))
        columns[3][1] = max(columns[3][1],len(record.PopWithCommas))
        columns[4][1] = max(columns[4][1],len(record.Region))
        columns[5][1] = max(columns[5][1],len(str(record.USHouseSeats)))

    #1c - print header text
    for header in columns:
        header[1]+=2
        sys.stdout.write(header[0].ljust(header[1])) #prints header text and spaces to match expected length
    sys.stdout.write("\n")

    #1d - sys.stdout.write(dividing bar b/w header text and state records
    for header in columns:
        for i in range(header[1]):
            sys.stdout.write("-")
    sys.stdout.write("\n")

    #1e - print state records
    for record in ListOfStates:
        sys.stdout.write(record.StateName.ljust(columns[0][1]))
        sys.stdout.write(record.CapitalCity.ljust(columns[1][1]))
        sys.stdout.write(record.Abbreviation.rjust(6).ljust((columns[2][1]))) #the rjust at here reflects expected style shown in Project 1 pdf instructions
        sys.stdout.write(record.PopWithCommas.rjust(12).ljust(columns[3][1])) #the rjust here reflects expected style shown in Project 1 pdf instructions
        sys.stdout.write(record.Region.ljust(columns[4][1]))
        sys.stdout.write(str(record.USHouseSeats).rjust(4).ljust((columns[5][1]))) #the rjust here reflects expected style shown in Project 1 pdf instructions
        sys.stdout.write("\n")
    sys.stdout.write("\n\n") #design doc quirk again
#end StateReport()



#Menu option 2 - Sort list of states by state name (using Quick sort)

#Menu option 3 - Sort list of states by population (using Radix sort)


#Menu option 4 - Individual state report
#4a binary search, if current list order is state name ABC
#4b sequential search, if list order is not currently state name ABC


#Menu option 5 - quit