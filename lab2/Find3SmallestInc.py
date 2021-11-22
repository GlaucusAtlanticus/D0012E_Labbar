# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX

# Step by Step
# 
# Input N, N >= 3
# Output [x < y < z] < N.rest
#
# 0. Base fall
#   If Input is 3 
#       Return x < y < z
# 1. Recursive call (N-1)  (antag att vi vet svaret för N-1)
# 2. Jämför N med svaret från (N-1)
#       Ifall N är mindre än något av {x<y<z} byt plats på dem
# 3. Retunera {x < y < z} (< rest)
# 
# #


# Takes N values returns the 3 smallest elements 
def IncrementalFindElement(lst):
    # base case calls help function that sort/orders the list
    if len(lst) == 3:
        x, y, z = SortSmallest(lst)
    # else do a recursive call
    else:
        x, y, z = IncrementalFindElement(lst[:-1])
    
    toCompare = lst[-1]

    # checks the last added element if it shall replace one of {x,y,z}
    if toCompare < y:
        if toCompare < x:
            return toCompare, x , y
        else:
            return x, toCompare, y
    else: 
        if toCompare < z:
            return x, y, toCompare
        else:
            return x, y, z

# help function takes a list of tree elements return them 
# in order so that x < y < z
def SortSmallest(lst):
    if lst[0] < lst[1] and lst[0] < lst[2]:
        if lst[1] < lst[2]:
            return lst[0], lst[1], lst[2]
        else: 
            return lst[0], lst[2], lst[1]
    elif lst[1] < lst[0] and lst[1] < lst[2]:
        if lst[0] < lst[2]:
            return lst[1], lst[0], lst[2]
        else: 
            return lst[1], lst[2], lst[0]
    else:
        if lst[0] < lst[1]:
            return lst[2], lst[0], lst[1]
        else: 
            return lst[2], lst[1], lst[0]


# Used to se if the program works
def main():
    lst = [5,3,5,7,1,34,54,6,6,45,7,4]
    print(IncrementalFindElement(lst))

#main()