def plusOne(digitsList):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    result = 0
    currentDigitIndex = 0
    #
    for i in digitsList:
        result += i * (10** (len(digitsList) - 1 - currentDigitIndex))
        currentDigitIndex += 1
    result += 1
    #
    print(result)
    

plusOne([1,2,3,4])