# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen



# help funk to bSort
def middle(l, r):               # tacks to int's 
    temp = (r - l)/2            # gets the difference divided by 2
    return round(temp)          # returns it as an int

# Binary sort
def bSort(list):
    sList = []                  # creates a empty list used for the sorted numbers

    if len(list) <= 1:
        return list

    if(list[0] > list[1]):      # if the secend element is larger then the first 
        sList.append(list[1])       # swaps place and puts them in sorted list
        sList.append(list[0])       
    else:                       # else
        sList.append(list[0])      # adds them in the order they come
        sList.append(list[1])

    if len(list) <= 2:
        return sList

    for x in list[2:]:          # goes thru from the 3 element to the end
        
        rPoint = (len(sList) -1)            # sets the right most point of the sorted list
        lPoint = 0                          # sets the left most point of the sorted list
        mPoint = middle(lPoint, rPoint)     # gets the middle of the sorted list

        if x >= sList[-1]:      # if element X is larger then sorted list[end] 
            sList.append(x)         # adds it to the end
            continue                # and goes to the next element

        if x <= sList[0]:       # if element X is smaller then sorted list[head] 
            sList = [x] + sList     # adds it to the begining 
            continue                # and goes to the next element

        # goes through the sorted list and finds element X place 
        while True:
            # if lPoint and rPoint are only one step from each outher 
            # insert element X in the middle 
            if (lPoint + 1) == rPoint:
                sList.insert(lPoint + 1, x)
                break
            
            # if element X is larger then mPoint
            # moves the lPoint to the mPoint
            elif (sList[mPoint] <= x):
                lPoint = mPoint
                mPoint += middle(lPoint, rPoint)
            # if element X is smaller then mPoint
            # moves the rPoint to the mPoint
            elif(sList[mPoint] >= x):
                rPoint = mPoint
                mPoint -= middle(lPoint, rPoint)
    return sList            # returns the sorted list
