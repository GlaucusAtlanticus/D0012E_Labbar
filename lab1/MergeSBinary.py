# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

from BinarySearch import bSort


# Splits lists into sublists, sorts them and then merges them.
def MergesortBin(list, k):
    #list1 = list[0:(round((len(list))/2))]
    #list2 = list[(round((len(list))/2)):(len(list))]
    print("Hi i am start of msortB k ", k)
    if k > 0:
        MergesortBin(list[0:(round((len(list))/2))], k-1)
        MergesortBin(list[(round((len(list))/2)):(len(list))], k-1)
        print("inside first if")
    else:
        print("begining of else",list)
        list1 = bSort(list[0:(round((len(list))/2))])
        list2 = bSort(list[(round((len(list))/2)):(len(list))])
        print("inside else")
        list3 = []
        while (len(list1) > 0) and (len(list2) > 0):
            if list1[0] < list2[0]:
                list3.append(list1[0])
                list1[0].pop
            else:
                list3.append(list2[0])
                list2[0].pop
        print("after while")
        #append what is left to list3
        if len(list1) > len(list2):
            list3.extend(list1)
        else:
            list3.extend(list2)
        print("before return")
        return list3




#############################################################
#               Rasmus Förslag                              #
#############################################################


# A merge sort funktion
def MergeSortBin(list, k):
    # if k = 0 do not divid list eny more sort it and return it
    if k == 0:
        listSort = bSort(list)                      # sort the list
        return listSort                             # and returns it
    # else divid list and send and merge the return 
    else:   
        halfList = round(len(list)/2)               # gets the midle of the list
        list1 = MergeSortBin(list[:halfList], k-1)  # recursive call whit the first part of the list
        list2 = MergeSortBin(list[halfList:], k-1)  # recursive call whit the secunde part of the list

        listSort = []                               # emty sorthed list

        # while loop that gears the lovest result whit each other 
        while (len(list1) > 0 and len(list2) > 0):
            # if the first element in list1 is smaller then list2
            # adds it to sorted list
            if list1[0] < list2[0]:
                listSort.append(list1[0])
                list1.pop(0)
            # else adds first element in list2 to sorted list
            else:
                listSort.append(list2[0])
                list2.pop(0)

        # if the first list have bean emtyd adds the secund list to sorted lst
        if len(list1) == 0:
            listSort.append(list2)
        # else adds first lst 
        else:
            listSort.append(list1)
        
        # returns sorted lst
        return listSort

