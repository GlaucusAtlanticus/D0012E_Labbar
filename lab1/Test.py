# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

# Import needed functions
import random
import time

# Imports the diffrent functions
from LinearSearch import Insertionsort
from BinarySearch import bSort
from MergeSBinary import MergesortBin
from MergeSBinary import TestMergesortbin
from MergeSNormal import Mergesort
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

def halfSort(size):
    halfSortList = []
    i = 1

    for x in range(1,size):
        halfSortList.append(i%10)
        i += 1

    return halfSortList


def sortedInput(size):
    tmpList = randomNR(size)
    tempList = bSort(tmpList)
    return tempList

# validates that the list is sorted
def validate(lst):

    while len(lst) > 1:
        if lst[0] > lst[1]:     # if the first number is larger then the next
            return False        # return false
        lst.pop(0)

    return True

# Starts Sorting algorithms and prints sorted list
#def Main():
def testMergeBinarySortIterative(N):
    f = open("Results.txt", "a")
    f.write("\n Merge BinarySort Iterative:\n")
    f.close
    k = 1  # k value

    # Sort the list for all valid values of k 0 to 20 and N(^2) from 1 to 20
    # k: number of sublists
    # N: size of list as a power of two

    while k < N:
        unSortList = randomNR(pow(2, N))

        #check that inputs are legal
        #if pow(2, k) >= len(unSortList):
        #    N = N + 1
        #    continue

        start_time = time.time()                    # Time at start of test
        sortList = MergesortBin(unSortList, pow(2, k))      # sort list using Mergesort binary
        runTime = time.time() - start_time          # time taken to sort the list

        minutes, seconds = divmod(runTime, 60)      # Get time taken in hours, minutes and seconds
        hours, minutes = divmod(minutes, 60)        #


        validated =  validate(sortList)             # Verify that the list got correctly sorted

        # print results to terminal
        print("k: 2^%s; N: %s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))
            
        #print(sortList)

        # write results to file
        f = open("Results.txt", "a")
        f.write("k: 2^%s; input length: 2^%s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))
        f.close
        k = k + 1
def testMergeLinearSort(N):
    f = open("Results.txt", "a")
    f.write("\n Merge LinearSort:\n")
    f.close

    print("testing mergesort linear")
    k = 1  # k value
    while k < N:

        unSortList = randomNR(pow(2, N))

        # check that inputs are legal
        #if pow(2, k) >= len(unSortList):
        #    print("bad batch")
        #    N = N + 1
        #    continue

        start_time = time.time()                    # Time at start of test
        sortList = MergesortLin(unSortList, pow(2, k))      # sort list using Mergesort linear
        runTime = time.time() - start_time          # time taken to sort the list

        minutes, seconds = divmod(runTime, 60)      # Get time taken in hours, minutes and seconds
        hours, minutes = divmod(minutes, 60)        #


        validated =  validate(sortList)             # Verify that the list got correctly sorted

        # print results to terminal
        print("k: 2^%s; N: %s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))

        # write results to file
        f = open("Results.txt", "a")
        f.write("k: 2^%s; input lenght: 2^%s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))
        f.close
        k = k + 1
def testMergeBinarySortRecursive(N):


    f = open("Results.txt", "a")
    f.write("\n Merge BinarySort Recursive:\n")
    f.close
    k = 1  # k value

    # Sort the list for all valid values of k 0 to 20 and N(^2) from 1 to 20
    # k: number of sublists
    # N: size of list as a power of two

    print("Testing TestMergesort")
    while k < N:
        unSortList = randomNR(pow(2, N))

        ##check that inputs are legal
        #if pow(2, k) >= len(unSortList):
        #    N = N + 1
        #    continue

        start_time = time.time()                    # Time at start of test
        sortList = TestMergesortbin(unSortList, pow(2, k))      # sort list using TestMergesortbin
        runTime = time.time() - start_time          # time taken to sort the list

        minutes, seconds = divmod(runTime, 60)      # Get time taken in hours, minutes and seconds
        hours, minutes = divmod(minutes, 60)        #

        validated =  validate(sortList)             # Verify that the list got correctly sorted

        # print results to terminal
        print("k: 2^%s; N: %s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))

        # write results to file
        f = open("Results.txt", "a")
        f.write("k: 2^%s; input length: 2^%s; Validated: %s; time = %d h, %d m, %s s;\n" %(k, N, validated, hours, minutes, seconds))
        f.close
        k = k + 1
def testPureMergeSort(N):
    f = open("Results.txt", "a")
    f.write("\n Pure Mergesort:\n")
    f.close

    # Sort the list for all valid values of k 0 to 20 and N(^2) from 1 to 20
    # N: size of list as a power of two

    print("Testing PureMergesort")
    unSortList = randomNR(pow(2, N))

    start_time = time.time()                    # Time at start of test
    sortList = Mergesort(unSortList)      # sort list using Mergesort
    runTime = time.time() - start_time          # time taken to sort the list

    minutes, seconds = divmod(runTime, 60)      # Get time taken in hours, minutes and seconds
    hours, minutes = divmod(minutes, 60)        #

    validated =  validate(sortList)             # Verify that the list got correctly sorted

    # print results to terminal
    print("N: %s; Validated: %s; time = %d h, %d m, %s s;\n" %(N, validated, hours, minutes, seconds))

    # write results to file
    f = open("Results.txt", "a")
    f.write("input length : 2^%s; Validated: %s; time = %d h, %d m, %s s;\n" %( N, validated, hours, minutes, seconds))
    f.close

def Main():
    
    N = 14           #will test up for list up to the size of 2^(maxSize)

    testPureMergeSort(N)
    #testMergeBinarySortIterative(N)
    testMergeBinarySortRecursive(N)
    testMergeLinearSort(N)
    
    


    












    


### Start Main ####################################################################
Main()