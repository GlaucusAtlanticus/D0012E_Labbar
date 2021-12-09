# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

from BinarySearch import bSort

# A merge sorter that takes help of a binary insertion sort
def MergesortBin(list, k):
    if k > len(list):
        print("wrong k value")
        return

    i = 0                           # a help int
    splitList = []                  # empty list that stores the splitted input

    if k == 0:
        return bSort(list)
    else:
        while (i*k) < len(list):        # runs as long as i*k is not outside the list
            splitList.append(list[(i*k) : ((i+1)*k)])   # adds a segment of input list to split list
            i += 1                      # increment i 

    splitListS = []                 # a empty list to store all sorted split list
    for X in splitList:
        splitListS.append(bSort(X)) # sorts all split list and adds them to splitListS

    sortedList = Sort(splitListS[0], splitListS[1])     # special case to handel the first 2 list in splitListS
    splitListS.pop(0)       # removes the list used in the special case
    splitListS.pop(0)       # removes the list used in the special case

    # sorts the list in splitListS and adds them to sortedList
    while len(splitListS) > 0:
        sortedList = Sort(sortedList, splitListS[0])
        splitListS.pop(0)

    # returns a sorted list
    return sortedList

# a sorting function
def Sort(list1, list2):
    templist = []

    while (len(list1) > 0) and (len(list2) > 0): # While still elements in both lists.
            
        # if the first element in list 1 is lesser than the first element in list 2,
        # append the first element in list 1 to output list and delete it from list1.
        if list1[0] < list2[0]:
            templist.append(list1[0])
            list1.pop(0)

            # As above but for list2.
        else:
            templist.append(list2[0])
            list2.pop(0)

    # if there is items left in one list append the list to the output list.
    if len(list1) > len(list2):
        templist.extend(list1)
    else:
        templist.extend(list2)

    return templist



###################################################################################
# Improvements to code
###################################################################################

def MergesortBinSecundIteration(list, k):
    if k > len(list):
        print("wrong k value")
        return

    i = 0                           # a help int
    splitList = []                  # empty list that stores the splitted input

    ## Splitter ###################################################################
    if k == 0:
        return bSort(list)
    else:
        while (i*k) < len(list):        # runs as long as i*k is not outside the list
            splitList.append(list[(i*k) : ((i+1)*k)])   # adds a segment of input list to split list
            i += 1                      # increment i 
    # Worst N    
    
    ## Sorter #####################################################################
    splitListS = []                 # a empty list to store all sorted split list
    for X in splitList:
        splitListS.append(bSort(X)) # sorts all split list and adds them to splitListS
    # Worst n/k * log n/k


    sortedList = fuckVadGorJag(splitList)
    while True:
        if len(sortedList) == 1:
            break 
        sortedList = fuckVadGorJag(sortedList)

    return sortedList

def fuckVadGorJag(lst):
    i = 0
    tempList = []
    while len(lst) != 0:
        try:
            tempList.append(Sort(lst[i], lst[i+1]))
            lst.pop(0)
            lst.pop(0)
        except:
            tempList.append(lst[0])
            lst.pop(0)
        i += 2
    
    return tempList

# a sorting function
def Sort(list1, list2):
    templist = []

    while (len(list1) > 0) and (len(list2) > 0): # While still elements in both lists.
            
        # if the first element in list 1 is lesser than the first element in list 2,
        # append the first element in list 1 to output list and delete it from list1.
        if list1[0] < list2[0]:
            templist.append(list1[0])
            list1.pop(0)

            # As above but for list2.
        else:
            templist.append(list2[0])
            list2.pop(0)

    # if there is items left in one list append the list to the output list.
    if len(list1) > len(list2):
        templist.extend(list1)
    else:
        templist.extend(list2)

    return templist
