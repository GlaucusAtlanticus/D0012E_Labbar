import math
import random
# https://stackoverflow.com/questions/57409385/how-do-i-see-the-time-it-took-to-run-my-program-in-visual-studio-code

### Lists ###################################################################################

Numbers = [5, 7, 10, 1, 4, 15, 3]

# Creates a large list with random numbers
RandomNumbers = []

for x in range(1, 10000):             # Size of list
    y = random.randint(1,10000)      # range of numbers
    RandomNumbers.append(y)             # Adds numbers to list

#### Functions ################################################################################

# Binary sort
def bSort(list):
    print("hej")

# Splits lists into sublists, sorts them and then merges them.
def MergesortBin(list):
    print("hej")

# Splits lists into sublists, sorts them and then merges them.
def MergesortLine(list):
    print("hej")


# Linear search
def Insertionsort(list):
  
    n = len(list)

    for j in range(0, n):
        
        while j > 0 and list[j-1] > list[j]:

            temp = list[j]                # This segment swaps j-1 and j
            list[j] = list[j-1]
            list[j-1] = temp

            j = j-1

# Splits lists into sublists, sorts them and then merges them.
def MergesortBin(list):
    # tolkade labspecen som att en mergsort ska hantera linjärt och en som hanterar bin
    print("hej")


# Linear Plain text
# Vårat input är en (osorterad) lista av N element 
# Vårat Output är en (sorterad) lista av N element
# 
# Hur funktionen funkar
# Funktionen funkar genom att man tar element (i)
# Jämför det elementet (j) som är den del av listan
#   ifall i < j 
##### More to come ######

# Starts Sorting algorithms and prints sorted list
def Main():
    # print("hej")
    # Insertionsort(RandomNumbers)
    print(RandomNumbers)


### Start Main ####################################################################
Main()

