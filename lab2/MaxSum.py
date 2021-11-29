# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX


# https://www.javatpoint.com/kadanes-algorithm-in-python#:~:text=Kadane%27s%20Algorithm%20is%20used%20to%20find%20the%20continuous,applying%20the%20brute-force%20approach%20and%20solving%20the%20problem.



#Gives maximum sum of subarrays in given list
def MaxSum(list):
    print("hej")




# Calculates sum between given indexes
def Sum(list, left, right):
    sum = 0

    while left != right:
        sum = sum + list[left]
        left + 1
    sum = sum + list[right]

# Calculates sum of split lists
def MaxSplit(list):
    maxSum = 0
    sum = 0
    startPointer = 0
    maxStartPointer = 0
    endPointer = 0

    for index in range (0, len(list)):
        sum = sum + list[index]

        if sum < 0:
            sum = 0
            startPointer = index + 1
        if sum > maxSum:
            maxSum = sum
            maxStartPointer = startPointer
            endPointer = index


    return maxSum, startPointer, endPointer


a = [0, 0, 0]

lista = [5,-3,5,7,1,-34,-54,6,-6,-45,7,4]

a[0], a[1], a[2] = MaxSplit(lista)

print(a[0])
print(a[1])
print(a[2])