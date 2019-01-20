from State import State
import csv
import sys

#TODO start of program docstring

#TODO start of program text and formatting

#Globals
ListOfStates = []
SortState = "Unsorted" # as in "the sort state of the list of states"

# States.csv import
with open('States.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
        ListOfStates.append( State(record["State"],record["Capital"],record["Abbreviation"],int(record["Population"]),record["Region"],int(record["US House Seats"])) )
print str(len(ListOfStates)) + " States Imported"





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
#end PrintStateReport(ListOfStates)



#Menu option 2 - Sort list of states by state name (using Quick sort)
def QuickSort(list):
    def partition(list,low,high): # referenced pseudocode here: https://en.wikipedia.org/wiki/Quicksort
        mid = (low + high)/2
        if list[mid] < list[low]:
            list[mid],list[low] = list[low],list[mid]
        if list[high] < list[low]:
            list[high],list[low] = list[low],list[high]
        if list[mid] < list[high]:
            list[mid],list[high] = list[high],list[mid]
        pivot = list[high]

        i = low-1
        for j in range(low, high):
            if list[j]<=pivot:
                i+=1
                list[i],list[j] = list[j],list[i]
        list[i+1],list[high]=list[high],list[i+1]
        return (i+1)

    def QuickSortAct(list,low,high):
        if low < high:
            intermediary = partition(list, low, high)
            QuickSortAct(list, low, intermediary)
            QuickSortAct(list, intermediary+1, high)

    QuickSortAct(list,0,len(list)-1)
    global SortState
    SortState = "QuickSort"
#end QuickSort(list)


#Menu option 3 - Sort list of states by population (using Radix sort)
def RadixSortStates():
    #referenced methodology here: https://en.wikipedia.org/wiki/Radix_sort#An_example
    global ListOfStates
    
    def RadixSortStatesAct(ListOfStates, DigitsPlaceToActOn): #digits place here is 1, 10, 100, etc.
        digitsList = [ [], [], [], [], [], [], [], [], [], []] #2d list. first level is 0-9 for digits, second level will be for records found with them
        intermediaryList = []
        for record in ListOfStates:
            digitsList[(record.Population/DigitsPlaceToActOn)%10].append(record)

        for digitPlace in digitsList:
            for record in digitPlace:
                intermediaryList.append(record)

        return intermediaryList
    
    highestPopulationNumber = max(record.Population for record in ListOfStates)
    currentDigitsPlace = 1
    while highestPopulationNumber/currentDigitsPlace > 0:
        ListOfStates = RadixSortStatesAct(ListOfStates,currentDigitsPlace)   
        currentDigitsPlace*=10
    global SortState
    SortState = "RadixSort"
#end RadixSortStates(ListOfStates)



#Menu option 4 - Individual state report
def GetState(): #returns State object, or string "State Name not found"
    SearchString = raw_input("Enter state name to search for: ")


    global ListOfStates
    global SortState
    #TODO 4a binary search, if current list order is state name ABC
    if(SortState=="QuickSort"):
        print "QuickSort"
        leftboundary = 0
        rightboundary = len(ListOfStates)-1

        while leftboundary <= rightboundary:
            currentSearchPosition = (leftboundary+rightboundary)/2
            if ListOfStates[currentSearchPosition].StateName < SearchString:
                leftboundary = currentSearchPosition+1
            elif ListOfStates[currentSearchPosition].StateName > SearchString:
                rightboundary = currentSearchPosition-1
            else:
                return ListOfStates[currentSearchPosition]
        return "State Name not found"

    #TODO 4b sequential search, if list order is not currently state name ABC
    else:
        print "Sequential Search"
        for record in ListOfStates:
            if record.StateName == SearchString:
                return record


#TODO Menu option 5 - quit


#TODO Menu loop


