# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

from BinarySearch import bSort
from BinarySearch import middle

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
        while (i*k) < len(list):        # runs ass long as i*k is not outside the list
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


##############################################################################################
#                           New Merge Code                                                   #
##############################################################################################

# A merge sorter that takes help of a binary insertion sort
def RMergesortBin(list, k):
    if k > len(list):                   # if K are larger then input print error msg and return
        print("wrong k value")
        return

    splitList = []                      # empty list that stores the splitted input

    if k == 0:                          # if K is 0 do a normal bSort   
        return bSort(list)
    else:                               # else split it in K size chunks
        splitList = splitter(list, k)
    
    halfSort = sortElement(splitList)   # sorts the splitted list
    
    sortedList = merger(halfSort)       # merges the sorted list
    while True:
        if len(sortedList) == 1:        # if the length of sortedList is 1 
            break                       # means that it have bin sorted

        sortedList = merger(halfSort)
    
    return sortedList                   # returns a sorted list

# takes a list of list and merges them two and two 
def merger(lst):
    tempList = []                       # temp help list

    while len(lst) > 0:                 # runs as long as input list is larger then 0
        if len(lst) == 1:               # if input list is one do special case
            tempList = tempList[:-1] + Sort(tempList[-1], lst)      # sorts it whit the last element in tempList
            break

        tempList = tempList + Sort(lst[0], lst[1])                  # sorts the two first list and adds them 
        lst.pop[0]                                                  # to the already sorted ones
        lst.pop[0]                                                  # and removes the ones that have bean used
    
    return tempList

# takes a list of list and calls a sorting func. fore each of the list 
# returns a list of sorted lists
def sortElement(lst):
    tempList = []
    for X in lst:                       # Gets each list in input list
        tempList.append(bSort(X))       # Sorts the list
    return tempList                     # and returns them

# tacks a list and a int, splits the list in K size chunks 
# returns a list of list
def splitter(list, k):
    i = 0                               
    tempList = []                       # a temp list
    while (i*k) < len(list):            # runs as long as i*k is not outside the list
        tempList.append(list[(i*k) : ((i+1)*k)])                    # adds a segment of input list to tempList
        i += 1   
    
    return tempList                     # returns a list of lists


# takes two lists sorts them and 
# return on list
def Sort(list1, list2):
    templist = []

    while (len(list1) > 0) and (len(list2) > 0):                    # While still elements in both lists.
            
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






##############################################################################################
#                           Test Merge                                                       #
##############################################################################################

def TestMergesortbin(lst, k):
    middlePoint = round(len(lst)/2)     # findes ware the middle of the list is

    if len(lst) < k:                    # if input list is smaller than K run normal sort 
        return bSort(lst)
    else:                               # else do  recursive call whit the first half of the list
                                        # then whit the secund half of the list
        list1 = TestMergesortbin(lst[:middlePoint], k)
        list2 = TestMergesortbin(lst[middlePoint:], k)

    sortList = []

    # sorts the two lists
    while (len(list1) > 0) and (len(list2) > 0):
        if list1[0] < list2[0]:
            sortList.append(list1[0])
            list1.pop(0)
        else:
            sortList.append(list2[0])
            list2.pop(0)

    # if there is items left in one list append the list to the output list.
    if len(list1) == 0:
        sortList.extend(list2)
    else:
        sortList.extend(list1)

    return sortList                     # returns a sorted list
    


##############################################################################################
#                           Old Code                                                         #
##############################################################################################
#####           Sät basfallet till K så ifall len(lst) <= K run bSort

# Splits lists into sublists, sorts them and then merges them.
def FuckMergesortBin(list, k):
    list1 = []  # first half of the list
    list2 = []  # second half of the list.
    outputList = []  # output list.

    halfList = round(len(list)/2)

    if k == 0:
        # when k = 0, split the list in two and input to bSort.
        list1 = bSort(list[:halfList])
        list2 = bSort(list[halfList:])
    else:
        #split the list in two and input to itself. Decreases k by 1.
        list1 = MergesortBin(list[:halfList], k-1)  #start to middle, 
        list2 = MergesortBin(list[halfList:], k-1)  # middle to end
    print("mamma")
    while (len(list1) > 0) and (len(list2) > 0): # While still elements in both lists.
            
        # if the first element in list 1 is lesser than the first element in list 2,
        # append the first element in list 1 to output list and delete it from list1.
        if list1[0] < list2[0]:
            outputList.append(list1[0])
            list1.pop(0)

            # As above but for list2.
        else:
            outputList.append(list2[0])
            list2.pop(0)

    # if there is items left in one list append the list to the output list.
    if len(list1) > len(list2):
        outputList.extend(list1)
    else:
        outputList.extend(list2)

    return outputList


