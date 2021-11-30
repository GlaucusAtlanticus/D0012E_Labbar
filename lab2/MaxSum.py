# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX

class Sum:
  def __init__(self, maxPrefix, maxSufix, totalSum, maxSum):
    self.maxPrefix = maxPrefix                          #the maximum sum of consecutive elements begining at the leftmost side
    self.maxSufix = maxSufix                            #the maximum sum of consecutive elements begining at the rightmost side
    self.totalSum = totalSum                            #The sum of all elements in the array
    self.maxSum = maxSum                                #the maximum sum of consecutive elements in the array
    

#p1 = Person("John", 36)

def MaxSum(list):
    length = len(list)                                  #lenght of list
    midpoint = int (length/ 2)                          #lenght of list / 2

    if length == 1:                                     #when the list consists of a single element return 
        s1 = Sum(list[0],list[0],list[0],list[0])       #all vars in Sum is set to the single elements value
        return s1
    else:
        leftList = list[:midpoint]                      # Divides list into two equaly sized parts
        rightList = list[midpoint:]

        L = MaxSum(leftList)                            # call upon itself for left and right subarray
        R = MaxSum(rightList)

        #totalsum                                       The sum of all elements in the array
        totalSum = L.totalSum + R.totalSum              

        #maxPrefix                                      the maximum sum of consecutive elements begining at the leftmost side
        if L.maxPrefix > L.totalSum + R.maxPrefix: 
            maxPrefix = L.maxPrefix
        else:
            maxPrefix = L.totalSum + R.maxPrefix
        
        #MaxSuffix                                      the maximum sum of consecutive elements begining at the rightmost side
        if R.maxSufix > R.totalSum + L.maxSufix:
            maxSufix = R.maxSufix
        else:
            maxSufix =  R.totalSum + L.maxSufix

        #MaxSum                                         the maximum sum of consecutive elements in the array
        if (R.maxSum > L.maxSum) and (R.maxSum > L.maxSufix + R.maxPrefix):     
            maxSum = R.maxSum
        elif (L.maxSum > R.maxSum) and (L.maxSum > L.maxSufix + R.maxPrefix):
            maxSum = L.maxSum
        else:
            maxSum = L.maxSufix + R.maxPrefix
        
        s1 = Sum(maxPrefix, maxSufix, totalSum, maxSum)

        return s1


def Main():
    lista = [5,-3,5,7,1,-10,20,6,-6,-45,7,4,-1,-25,10,-40]
    s1 = MaxSum(lista)
    print(s1.maxSum)
Main()