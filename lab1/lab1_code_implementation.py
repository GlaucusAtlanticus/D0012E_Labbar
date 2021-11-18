# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Import needed functions
import random
import time

# Imports the diffrent functions
from LinearSearch import Insertionsort
from BinarySearch import bSort, TestBSort
from MergeSBinary import MergesortBin
from MergeSLinear import MergesortLin 



### Lists ###################################################################################

Numbers = [5, 7, 7, 10, 1, 4, 15, 3]

# Creates a large list with random numbers
RandomNumbers = []
print("creating rand num")
for x in range(1, 10000):             # Size of list
    y = random.randint(1,10000)         # range of numbers
    RandomNumbers.append(y)             # Adds numbers to list
print("don creating rand num")


# validates that the list is sorted
def validate(lst):

    while len(lst) > 1:
        if lst[0] > lst[1]:     # if the first number is larger then the next
            return False        # return false
        lst.pop(0)

    return True

# Starts Sorting algorithms and prints sorted list
def Main():

    k = 15

    # start timer
    start_time = time.time()
    
    ### the diffrent functions ###
    #list = MergesortLin(RandomNumbers, k)
    #list = MergesortBin(RandomNumbers, k)
    #list = Insertionsort(RandomNumbers)
    list = bSort(RandomNumbers)
    # prints time to run sorthing method
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    if len(list) == len(RandomNumbers):
        print("True")
    else:
        print("False")

    # validates the list    
    print(validate(list))

### Start Main ####################################################################
Main()


#for k in range (0, 20)