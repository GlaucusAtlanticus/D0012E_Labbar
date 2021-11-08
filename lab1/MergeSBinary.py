# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

from BinarySearch import bSort

# Splits lists into sublists, sorts them and then merges them.
def MergesortBin(list, k):
    list1 = []  # first half of the list
    list2 = []  # second half of the list.
    outputList = []  # output list.

    halfList = round(len(list)/2)

    if k == 0:
        # when k = 0, split the list in two and input to bsort.
        list1 = bSort(list[:halfList])
        list2 = bSort(list[halfList:])
    else:
        #split the list in two and input to itself. Decreses k by 1.
        list1 = MergesortBin(list[:halfList], k-1)  #start to middle, 
        list2 = MergesortBin(list[halfList:], k-1)  # middle to end
    
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

    # if there is items left in one list append the list to the ouptput list.
    if len(list1) > len(list2):
        outputList.extend(list1)
    else:
        outputList.extend(list2)

    return outputList


