# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX





# help function takes a list of tree elements return them 
# in order so that x < y < z
# Input: [x, y, z]
# Output: Sorted input, low-high
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