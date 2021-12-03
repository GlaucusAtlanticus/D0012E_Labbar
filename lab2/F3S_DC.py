# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX

from SortSmallest import SortSmallest



#   Step by Step
    # 
    # Input N, N >= 3
    # Output [x < y < z] < N.rest
    #
    # 0. Base fall
    #   If Input =< 5 
    #       Return x < y < z
    # 1. Divide input in to equal size parts 
    # 2. Do recursive call on the first half(N / 2 [lower])
    # 3. Do recursive call on the secund half(N / 2 [upper])
    # 2. Compare awnser from first half whit secund half
    # 3. Return {x < y < z} (< rest)
    # 
    # #

# Takes n values and returns the 3 smallest
def DC_FSE(lst):    # Divide and Conquer Find Smallest Element
    lstOne = [0, 0, 0]                  # Help List
    lstTwo = [0, 0, 0]                  # Help List
    if len(lst) == 3:                   # If Input is 3 sort the input
        x, y, z = SortSmallest(lst)
        return x, y, z                  # return the input sorted
    else:                               # else
        halfList = round(len(lst)/2)    # get the half point of the list
        lstOne[0], lstOne[1], lstOne[2] = DC_FSE(lst[:halfList])    # Recursive call whit the first part of the list
        lstTwo[0], lstTwo[1], lstTwo[2] = DC_FSE(lst[halfList:])    # Recursive call whit the secund part of the list
        
        #x1, y1, z1 = DQ_FindSmallestElement(lst[:halfList])
        #lstOne = [x1, y1, z1]
        #x2, y2, z2 = DQ_FindSmallestElement(lst[halfList:])
        #lstTwo = [x2, y2, z2]

    lstAns = []                         # awnser list to store the correct values
    for elmOne in lstOne:               # Goes through all elements in lstOne
        for elmTwo in lstTwo:           # Goes through all elements in lstTwo
            if elmTwo < elmOne:         # If element from lstTwo is smaller then element from lstOne
                lstAns.append(elmTwo)   #   add element from lstTwo to awnser
                lstTwo.remove(elmTwo)   #   remove element from lstTwo (to not count it twice)
                break                   #   and jumps to the next element from lstOne
        lstAns.append(elmOne)           # else add element from lstOne to the awnser

    return lstAns[0], lstAns[1], lstAns[2]      # returns the values


def main():
    lst = [5,3,5,7,1,34,54,6,6,45,7,4]
    print(DC_FSE(lst))

main()
