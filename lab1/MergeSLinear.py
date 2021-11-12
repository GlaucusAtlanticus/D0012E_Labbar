# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

from LinearSearch import Insertionsort


# A merge sorter that takes help of a linear insertion sort
def MergesortLin(list, k):
    if k > len(list):
        print("wrong k value")
        return
        
    i = 0                           # a help int
    splitList = []                  # empty list that stores the splitted input
    
    if k == 0:
            return Insertionsort(list)
    else:
        while (i*k) < len(list):        # runs ass long as i*k is not outside the list
            splitList.append(list[(i*k) : ((i+1)*k)])   # adds a segment of input list to split list
            i += 1                      # increment i 

    splitListS = []                 # a empty list to store all sorted split list
    for X in splitList:
        splitListS.append(Insertionsort(X))             # sorts all split list and adds them to splitListS

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
#                           Old Code                                                         #
##############################################################################################
# Splits lists into sublists, sorts them and then merges them.
def FuckMergesortLin(list, k):
    list1 = []  # first half of the list
    list2 = []  # second half of the list.
    outputList = []  # output list.

    halfList = round(len(list)/2)

    if k == 0:
        # when k = 0, split the list in two and input to Insertionsort.
        list1 = Insertionsort(list[:halfList])
        list2 = Insertionsort(list[halfList:])
    else:
        #split the list in two and input to itself. Decreases k by 1.
        list1 = FuckMergesortLin(list[:halfList], k-1)  #start to middle, 
        list2 = FuckMergesortLin(list[halfList:], k-1)  # middle to end
    
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
