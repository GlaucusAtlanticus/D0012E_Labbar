import math



### Lists ###

Numbers = [5, 7, 10, 1, 4, 15, 3]


#### Functions ###

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
def MergesortBin(list):
    print("hej")

# Splits lists into sublists, sorts them and then merges them.
def MergesortLine(list):
    print("hej")


# Linear search
def Insertionsort(list):
  
    n = len(list)


# Splits lists into sublists, sorts them and then merges them.
def MergesortBin(list):
    # tolkade labspecen som att en mergsort ska hantera linjärt och en som hanterar bin
    print("hej")

# Linear search
def Insertionsort(list):
    n = len(list)

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
    print(Numbers)
    print("hej")
    print(bSort(Numbers))


### Start Main ###
Main()

