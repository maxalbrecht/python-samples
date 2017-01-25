def leftAndRightMost(originalnumList, firstFoundIndex, target):
    currentIndex = firstFoundIndex
    leftMost = 0
    rightMost = 0
    while currentIndex >= 0 and originalnumList[currentIndex] == target:
        leftMost = currentIndex
        currentIndex -= 1
    currentIndex = firstFoundIndex
    while currentIndex < len(originalnumList)and originalnumList[currentIndex] == target:
        rightMost = currentIndex
        currentIndex += 1
    #
    return [leftMost, rightMost]
    
    
def searchRange(numList, target, originalnumList = [], referencePoint = 0):
    """
    :type numbs: List[int]
    :type target: int
    :rtype: List[int]
    """
    Left = 0
    Right = len(numList) -1
    midpoint = Right/2
    if len(originalnumList) == 0:
        originalnumList = numList   
    #
    if target != numList[midpoint] and len(numList) == 1:
        return [-1,-1]
    if target == numList[midpoint] and len(numList) >= 1:
        referencePoint += (len(numList) - 1) / 2
        #print(str(numList[midpoint]) + '; total reference point = ' + str(referencePoint))
        #return referencePoint
        return leftAndRightMost(originalnumList, referencePoint, target)
    #
    elif target < numList[midpoint] and len(numList) >= 1:
        Right = midpoint
        if originalnumList[referencePoint] < target:
            referencePoint += (len(numList) - 1)/2
        if originalnumList[referencePoint] > target:
            referencePoint -= (len(numList) - 1)/2
        return searchRange(numList[Left:Right+1], target, originalnumList, referencePoint)
    #
    elif target > numList[midpoint] and len(numList) >= 1:
        if len(numList) ==2:
            referencePoint += (len(numList)) / 2
            Left = midpoint + 1
        else:
            referencePoint += (len(numList) - 1) / 2
            Left = midpoint
        return searchRange(numList[Left:Right+1], target, originalnumList, referencePoint)
    #
    else:
        return [-1,-1]
                  
                         
                            
                               
                                  
                                     
                                        
                                              
print(searchRange([1,2,4,5,6,7,8,9], 5))

