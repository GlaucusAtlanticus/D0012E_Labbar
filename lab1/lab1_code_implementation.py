import math
import random

# https://stackoverflow.com/questions/57409385/how-do-i-see-the-time-it-took-to-run-my-program-in-visual-studio-code

### Lists ###################################################################################

Numbers = [5, 7, 10, 1, 4, 15, 3]

# Creates a large list with random numbers
RandomNumbers = []

for x in range(1, 10000):             # Size of list
    y = random.randint(1,10000)      # range of numbers
    RandomNumbers.append(y)             # Adds numbers to list

#### Functions ################################################################################

# help funk to bSort
def middle(l, r):       # tacks to ints 
    temp = (r - l)/2    # gets the diffrence divided by 2
    return round(temp)  # returns it as an int

# Binary sort
def bSort(list):
    sList = []                  # creates a emty list used for the sorthed numbers

    if len(list) <= 1:
        return list

    if(list[0] > list[1]):      # if the secend elemet is larger then the first 
        sList.append(list[1])       # swapps place and puts them in sorted list
        sList.append(list[0])       
    else:                       # else
        sList.append(list[0])      # adds them in the order they come
        sList.append(list[1])

    if len(list) <= 2:
        return sList

    for x in list[2:]:          # goes thru frome the 3 elemnt to the end
        rPoint = (len(sList) -1)            # sets the right most point of the sorted list
        lPoint = 0                          # sets the left most point of the sorted list
        mPoint = middle(lPoint, rPoint)     # gets the middle of the sorted list

        if x >= sList[-1]:      # if element X is larger then sorted list[end] 
            sList.append(x)         # adds it to the end
            continue                # and goes to the next element

        if x <= sList[0]:       # if element X is smaller then sorted list[head] 
            sList = [x] + sList     # adds it to the begining 
            continue                # and goes to the next element


        # goes throgh the sorted list and finds element X place 
        while True:
            # if lPoint and rPoint are only one step from each outher 
            # insert element X in the middle 
            if (lPoint + 1) == rPoint:
                sList.insert(lPoint + 1, x)
                break
            
            # if element X is larger then mPoint
            # moves the lPoint to the mPoint
            if (sList[mPoint] < x):
                lPoint = mPoint
                mPoint = middle(lPoint, rPoint)
            # if element X is smaller then mPoint
            # moves the rPoint to the mPoint
            elif(sList[mPoint] > x):
                rPoint = mPoint
                mPoint = middle(lPoint, rPoint)

    return sList            # returns the sorthed list
            
# Splits lists into sublists, sorts them and then merges them.
def MergesortBin(list, k):
    #list1 = list[0:(round((len(list))/2))]
    #list2 = list[(round((len(list))/2)):(len(list))]
    if k > 0:
        MergesortBin(list[0:(round((len(list))/2))], k-1)
        MergesortBin(list[(round((len(list))/2)):(len(list))], k-1)
    else:
        list1 = bSort(list[0:(round((len(list))/2))])
        list2 = bSort(list[(round((len(list))/2)):(len(list))])

        list3 = []
        while (len(list1) > 0) and (len(list2) > 0):
            if list1[0] < list2[0]:
                list3.append(list1[0])
                list1[0].pop
            else:
                list3.append(list2[0])
                list2[0].pop

        #append what is left to list3
        if len(list1) > len(list2):
            list3.extend(list1)
        else:
            list3.extend(list2)
        return list3

# Splits lists into sublists, sorts them and then merges them.
def MergesortLine(list, k):
    print("hej")


# Linear search
def Insertionsort(list):
  
    n = len(list)

    for j in range(0, n):
        
        while j > 0 and list[j-1] > list[j]:

            temp = list[j]                # This segment swaps j-1 and j
            list[j] = list[j-1]
            list[j-1] = temp

            j = j-1

# Splits lists into sublists, sorts them and then merges them.
def MergesortBin(list, k):
    # tolkade labspecen som att en mergsort ska hantera linjärt och en som hanterar bin
    print("hej")

# Linear Plain text
# Vårat input är en (osorterad) lista av N element 
# Vårat Output är en (sorterad) lista av N element
# 
# Hur funktionen funkar
# Funktionen funkar genom att man tar element (i)
# Jämför det elementet (j) som är den del av listan
#   ifall i > j 
#       swapp
#       iterate i 
#   else 
#       j++
##### More to come ######

# Starts Sorting algorithms and prints sorted list
def Main():
    k = 2

    # MergesortBin(RandomNumbers, k)
    list =  MergesortLine(RandomNumbers, k)
    # bSort(RandomNumbers)
    # Insertionsort(RandomNumbers)

    print(list)

### Start Main ####################################################################
Main()

