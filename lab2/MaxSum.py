# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX


# https://www.javatpoint.com/kadanes-algorithm-in-python#:~:text=Kadane%27s%20Algorithm%20is%20used%20to%20find%20the%20continuous,applying%20the%20brute-force%20approach%20and%20solving%20the%20problem.



#Gives maximum sum of subarrays in given list
def MaxSum(list):

    length = len(list)

    leftList = list[:length]                        # Divides lists
    rightList = list[length:]

    leftValue = MaxSplit(leftList)                  # Gets max sum of each split list and their indexes
    rightValue = MaxSplit(rightList)

    inbetween = Sum(list, leftValue[2], rightValue[1] + length/2)           # Calculates the sum between the 2 maxsums

    if abs(inbetween) > leftValue[0] or abs(inbetween) > rightValue[0]:     # If the sum inbetween has a larger absolute value
        if leftValue[0] < rightValue[0]:                                    # return either maxsum depending on their size
            return rightValue[0]
        else:
            return leftValue[0]
    else:
        return inbetween + leftValue[0] + rightValue[0]                     # Returns both sums combined + inbetween sum if it is larger

# Calculates sum between given indexes
def Sum(list, left, right):     
    sum = 0                                       # Sets sum to 0

    while left != right:                          # Goes through all elements until last element equals current
        sum = sum + list[left]                    # Adds element value to sum
        left + 1                                  # Increases index
    sum = sum + list[right]                       # Adds lasts element

# Calculates sum of split lists
def MaxSplit(list):                               
    maxSum = 0                                    # Sets all variables to 0
    sum = 0
    startPointer = 0
    maxStartPointer = 0
    endPointer = 0

    for index in range (0, len(list)):            # Goes through all elements
        sum = sum + list[index]                   # Adds element value to sum

        if sum < 0:                               # Resets sum to 0 if it gets negetive
            sum = 0
            startPointer = index + 1              # Updates new start pointer
        if sum > maxSum:                          # Update maxsum if sum is higher
            maxSum = sum                          
            maxStartPointer = startPointer        # Updates maxstartpointer
            endPointer = index                    # Sets end index of sum  


    return maxSum, maxStartPointer, endPointer    # Returns


a = [0, 0, 0]

lista = [5,-3,5,7,1,-34,-54,6,-6,-45,7,4]

a[0], a[1], a[2] = MaxSplit(lista)

print(a[0])
print(a[1])
print(a[2])