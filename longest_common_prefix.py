def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    currentPrefix = ''
    currentIndex = 0
    stillCommonPrefix = True
    shortestLength = len(min(strs))
    firstString = strs[0]
    #
    testPrefix = ''
    while currentIndex <= shortestLength and stillCommonPrefix == True:
        testPrefix = firstString[:currentIndex]
        for i in strs:
            if testPrefix != i[:currentIndex]:
                stillCommonPrefix = False
            else:
                currentPrefix = testPrefix
        currentIndex += 1
    #
    print(currentPrefix)

longestCommonPrefix(['abcdef', 'abcd', 'abc'])