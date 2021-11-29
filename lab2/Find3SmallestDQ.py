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
#   If Input =< 5 
#       Return x < y < z
# 1. Divide input in to equal size parts 
# 2. Do recursive call on the first half(N / 2 [lower])
# 3. Do recursive call on the second half(N / 2 [upper])
# 2. Compare awnser from first half with second half
# 3. Return {x < y < z} (< rest)
# 
# #

def DQ_FindSmallestElement(lst):
    lstOne = [0,0,0]
    lstTwo = [0,0,0]
    if len(lst) == 3:
        x, y, z, = SortSmallest(lst)
        return x, y, z
    else:
        halfList = round(len(lst)/2)
        x1, y1, z1 = DQ_FindSmallestElement(lst[:halfList])
        lstOne = [x1, y1, z1]
        x2, y2, z2 = DQ_FindSmallestElement(lst[halfList:])
        lstTwo = [x2, y2, z2]

    lstAnswer = []
    for elementOne in lstOne:
        for elementTwo in lstTwo:
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

