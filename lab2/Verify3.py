# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX

from SortSmallest import SortSmallest



# Checks if Find3Smallest Algorithm is correct.
#   
# Input: Full list, list of 3 elements in list
# Output: True/False
def Verify(lst, xyz):
   
    if xyz == SortSmallest(xyz):
        for element in lst:
            
            if element < xyz[0]:
                return False
            
            
                
    else: 
        return False