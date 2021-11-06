# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

# Import needed funktions
import math     # not needed?
import random
import time

# Imports the diffrent funktions
from LinearSearch import Insertionsort
from BinarySearch import bSort
from MergeSBinary import MergesortBin
from MergeSLinear import MergesortLin

# https://stackoverflow.com/questions/57409385/how-do-i-see-the-time-it-took-to-run-my-program-in-visual-studio-code

### Lists ###################################################################################

Numbers = [5, 7, 7, 10, 1, 4, 15, 3]

# Creates a large list with random numbers
RandomNumbers = []
print("creating rand num")
for x in range(1, 1000000):             # Size of list
    y = random.randint(1,10000)      # range of numbers
    RandomNumbers.append(y)             # Adds numbers to list
print("don creating rand num")


# validates that the list is sorted
def validate(lst):

    while len(lst) > 1:
        if lst[0] > lst[1]:
            return False
        lst.pop(0)

    return True


# Starts Sorting algorithms and prints sorted list
def Main():

    k = 2

    # start timer
    start_time = time.time()
    
    ### the diffrent funktions ###
    #list = MergesortLin(RandomNumbers, k)
    #list = MergesortBin(RandomNumbers, k)
    #list = bSort(RandomNumbers)
    list = Insertionsort(RandomNumbers)

    # prints time to run sorthing method
    print("Process finished --- %s seconds ---" % (time.time() - start_time))

    # validates the list    
    print(validate(list))

### Start Main ####################################################################
Main()

