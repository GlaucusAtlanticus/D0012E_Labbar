# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

from BinarySearch import bSort

def MergesortBin(list, k):

    i = 0
    splitList = []
    while (i*k) < len(list):
        if i == 0:
            splitList.append(specialSplit(list, k))
        else:
            splitList.append(list[(i*k) : ((i+1)*k)])
        i += 1
    
    splitListS = []
    for X in splitList:
        splitListS.append(bSort(X))

    sortedList = specialSort(splitListS[0], splitListS[1])
    splitListS.pop(0)
    splitListS.pop(0)

    while len(splitListS) > 0:
        sortedList = specialSort(sortedList, splitListS[0])
        splitListS.pop(0)

    print(sortedList)
    return sortedList


def specialSplit(list, k):
    tempList = list[:k]
    return tempList


def specialSort(list1, list2):
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


