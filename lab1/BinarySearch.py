# Edvin Petterson
# Jonatan Trefill
# Rasmus Jacobsen



# help funk to bSort
def middle(l, r):               # tacks to ints 
    temp = (r - l)/2            # gets the diffrence divided by 2
    return round(temp)          # returns it as an int

# Binary sort
def bSort(list):
    #tracesrInt = 1
    sList = []                  # creates a emty list used for the sorthed numbers

    if len(list) <= 1:
        return list

    if(list[0] > list[1]):      # if the secend elemet is larger then the first 
        sList.append(list[1])       # swapps place and puts them in sorted list
        sList.append(list[0])       
    else:                       # else
        sList.append(list[0])      # adds them in the order they come
        sList.append(list[1])

    if len(list) <= 2:
        return sList

    for x in list[2:]:          # goes thru frome the 3 elemnt to the end
        print(len(sList))
        #print("elemts run ", tracesrInt)

        rPoint = (len(sList) -1)            # sets the right most point of the sorted list
        lPoint = 0                          # sets the left most point of the sorted list
        mPoint = middle(lPoint, rPoint)     # gets the middle of the sorted list

        #tracesrInt += 1
        if x >= sList[-1]:      # if element X is larger then sorted list[end] 
            sList.append(x)         # adds it to the end
            continue                # and goes to the next element

        if x <= sList[0]:       # if element X is smaller then sorted list[head] 
            sList = [x] + sList     # adds it to the begining 
            continue                # and goes to the next element

        #print("before loop")
        # goes throgh the sorted list and finds element X place 
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
        #print("after loop")
    return sList            # returns the sorthed list

def FuckbSort(list):
    tracesrInt = 1

    sList = []                  # creates a emty list used for the sorthed numbers

    if len(list) <= 1:          # if the list is 1 ore smaller return as is
        return list

    if(list[0] > list[1]):      # if the secend elemet is larger then the first 
        sList.append(list[1])       # swapps place and puts them in sorted list
        sList.append(list[0])       
    else:                       # else
        sList.append(list[0])      # adds them in the order they come
        sList.append(list[1])

    if len(list) <= 2:          # if list is 2 ore smaller return as is
        return sList

    list.pop(0)
    list.pop(0)

    while len(list) > 0:        # runs as long as the in list is not empty 
        print("elemts run ", tracesrInt)

        tracesrInt += 1
        if list[0] >= sList[-1]:      # if element X is larger then sorted list[end] 
            sList.append(list[0])         # adds it to the end
            list.pop(0)
            continue                # and goes to the next element

        if list[0] <= sList[0]:       # if element X is smaller then sorted list[head] 
            sList = [list[0]] + sList     # adds it to the begining 
            list.pop(0)
            continue                # and goes to the next element

        rPoint = (len(sList) -1)            # sets the right most point of the sorted list
        lPoint = 0                          # sets the left most point of the sorted list
        mPoint = middle(lPoint, rPoint)     # gets the middle of the sorted list

        #print("before loop")
        # goes throgh the sorted list and finds element X place 
        while True:
            # if lPoint and rPoint are only one step from each outher 
            # insert element X in the middle 
            if (lPoint + 1) == rPoint:
                sList.insert(lPoint + 1, list[0])
                list.pop(0)
                break
            
            # if element X is larger then mPoint
            # moves the lPoint to the mPoint
            elif (sList[mPoint] <= list[0]):
                lPoint = mPoint
                mPoint += middle(lPoint, rPoint)
            # if element X is smaller then mPoint
            # moves the rPoint to the mPoint
            elif(sList[mPoint] >= list[0]):
                rPoint = mPoint
                mPoint -= middle(lPoint, rPoint)
        #print("after loop")
    return sList            # returns the sorthed list
