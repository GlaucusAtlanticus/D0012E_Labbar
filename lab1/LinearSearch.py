# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen


# Linear search
def Insertionsort(list):
  
    n = len(list)

    for j in range(0, n):
        
        while j > 0 and list[j-1] > list[j]:

            temp = list[j]                # This segment swaps j-1 and j
            list[j] = list[j-1]
            list[j-1] = temp

            j = j-1

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