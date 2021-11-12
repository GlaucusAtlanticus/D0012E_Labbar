# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen


# Linear search
def Insertionsort(list):
  
    n = len(list)                         # Length of list

    for j in range(1, n):                 # Iterates Through the entire list, will make it so the left side of the for loop value is sorted.

        while j > 0 and list[j-1] > list[j]:        # Swaps 2 list elements if lower index element is larger. 

            temp = list[j]                # This segment swaps j-1 and j
            list[j] = list[j-1]
            list[j-1] = temp

            j = j-1                       # Lowers index value, ultimately towards 0 or until a smaller number is found.
    return list

# Linear Plain text
# Vårat input är en (osorterad) lista av N element 
# Vårat Output är en (sorterad) lista av N element
# 
# Hur funktionen funkar
# Funktionen funkar genom att man tar element (i)
# Jämför det elementet (j) som är den del av listan
#   ifall i > j 
#       swapp
#       iterate i 
#   else 
#       j++
##### More to come ######