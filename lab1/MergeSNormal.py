# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen



# Splits lists into sublists, sorts them and then merges them.
def Mergesort(list):
    outputList = []                 # output list.

    halfList = round(len(list)/2)   # finds where the middle is

    if len(list) == 1:              # if the input list only have one element 
        return list                 # return that list
    else:
        list1 = Mergesort(list[:halfList])  # recursive call whit the first half of the list
        list2 = Mergesort(list[halfList:])  # recursive call whit the secend half of the list


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

    return outputList               # returns the sorted list