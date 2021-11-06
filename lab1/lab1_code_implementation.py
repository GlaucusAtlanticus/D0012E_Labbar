import math
import random
import time


from LinearSearch import Insertionsort
from BinarySearch import bSort
from MergeSBinary import MergesortBin
from MergeSLinear import MergesortLin

# https://stackoverflow.com/questions/57409385/how-do-i-see-the-time-it-took-to-run-my-program-in-visual-studio-code

### Lists ###################################################################################

Numbers = [5, 7, 10, 1, 4, 15, 3]
Num = [2811, 2823, 2835, 3686, 5967, 8158, 765, 6356, 1954, 5188, 8317, 2762, 6898, 7525, 6155, 7585, 560, 4590, 6837, 5228, 9840, 4409, 6286, 3727, 9278, 1458, 629, 7973, 3634, 7634, 6360, 396, 6014, 9049, 9345, 965, 5696, 7576, 7279, 480, 335, 6313, 9775, 8677, 6180, 3021, 2469, 2495, 2972, 5141, 4764, 2589, 2469, 2824, 7442, 2560, 
7953, 8025, 9995, 1681, 8294, 2170, 4977, 467, 4814, 6785, 3537, 2879, 6129, 1497, 6832, 9806, 9131, 9317, 1106, 6127, 8213, 8904, 9397, 4467, 9144, 3512, 9917, 5056, 4616, 5675, 6919, 529, 821, 3285, 8158, 9486, 7731, 6147, 1872, 8621, 6328, 3589, 3148]

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
    print(len(RandomNumbers))

    start_time = time.time()
    k = 2

    # MergesortLin(RandomNumbers, k)
    #list =  MergesortBin(RandomNumbers, k)
    list = bSort(RandomNumbers)
    #list = Insertionsort(RandomNumbers)

    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    
    print(len(list))

    print(validate(list))

### Start Main ####################################################################
Main()

