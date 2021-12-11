# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX

from SortSmallest import SortSmallest



# Step by Step
# 
# Input N, N >= 3
# Output [x < y < z] < N.rest
#
# 0. Base fall
#   If Input == 3 
#       Return x < y < z
# 1. Divide input in to equal size parts 
# 2. Do recursive call on the first half(N / 2 [lower])
# 3. Do recursive call on the second half(N / 2 [upper])
# 2. Compare awnser from first half with second half
# 3. Return {x < y < z} (< rest)
# 
# #

# Takes n values and returns the 3 smallest
def DQ_FindSmallestElement(lst):
    lstOne = [0, 0, 0]                  # Help List
    lstTwo = [0, 0, 0]                  # Help List
    if len(lst) == 3:                   # If Input is 3 sort the input
        x, y, z = SortSmallest(lst)
        return x, y, z                  # return the input sorted
    else:                               # else
        halfList = round(len(lst)/2)
        lstOne[0], lstOne[1], lstOne[2] = DQ_FindSmallestElement(lst[:halfList])
        lstTwo[0], lstTwo[1], lstTwo[2] = DQ_FindSmallestElement(lst[halfList:])
        

    lstAnswer = []                                          # Holds return values
    for elementOne in lstOne:                               # Checks if elements in lstTwo are smaller
        for elementTwo in lstTwo:                           #
            if elementTwo < elementOne:
                lstAnswer.append(elementTwo)
                lstTwo.remove(elementTwo)
                break
        lstAnswer.append(elementOne)
    return lstAnswer[0], lstAnswer[1], lstAnswer[2]


def main():
    lst = [5,3,5,7,1,34,54,6,6,45,7,4]
    print(DQ_FindSmallestElement(lst))

main()

