# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

# Import needed funktions
import random
import time

# Imports the diffrent funktions
from LinearSearch import Insertionsort
from BinarySearch import bSort
from MergeSBinary import MergesortBin
from MergeSLinear import MergesortLin


### Lists ###################################################################################

Numbers = [5, 7, 7, 10, 1, 4, 15, 3]

# Creates a large list with random numbers
def randomNR(size):    
    RandomNumbers = []
    print("creating rand num")
    for x in range(1, size):             # Size of list
       y = random.randint(1,size)         # range of numbers
       RandomNumbers.append(y)             # Adds numbers to list
    print("done creating rand num")
    return RandomNumbers


# validates that the list is sorted
def validate(lst):

    while len(lst) > 1:
        if lst[0] > lst[1]:     # if the first number is larger then the next
            return False        # return false
        lst.pop(0)

    return True

# Starts Sorting algorithms and prints sorted list
def Main():
    f = open("Results.txt", "a")
    f.write("\n BSORT:\n")
    f.close
    k = 20  # k value
    while k >= 0:
        N = 1 # power of two size of random list
        while N <= 20:
            unSortList = randomNR(pow(2, N))
            if k >= len(unSortList):
                N = N + 1
                continue

            start_time = time.time()
            sortList = MergesortBin(unSortList, k)
            runTime = time.time() - start_time
            minutes, seconds = divmod(runTime, 60)
            hours, minutes = divmod(minutes, 60)


            validated =  validate(sortList)
            print("k: %s; N: %s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))
            print(len(sortList))
            f = open("Results.txt", "a")
            f.write("k: %s; input lenght : 2^%s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))
            f.close
            N = N + 1
        k = k -1
    
    f = open("Results.txt", "a")
    f.write("\n LSORT:\n")
    f.close

    print("NEXT")
    k = 20  # k value
    while k >= 0:
        N = 1 # power of two size of random list
        while N <= 20:
            unSortList = randomNR(pow(2, N))
            if k >= len(unSortList):
                print("bad batch")
                N = N + 1
                continue

            start_time = time.time()

            sortList = MergesortLin(unSortList, k)
            
            runTime = time.time() - start_time
            minutes, seconds = divmod(runTime, 60)
            hours, minutes = divmod(minutes, 60)


            validated =  validate(sortList)
            print("k: %s; N: %s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))
            print(len(sortList))
            f = open("Results.txt", "a")
            f.write("k: %s; input lenght : 2^%s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))
            f.close
            N = N + 1
        k = k -1
    












    


### Start Main ####################################################################
Main()