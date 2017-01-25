def lengthOfLastWord(s):
    import string
    """
    :type s: str
    :rtype: int
    """
    stringList = s.split()
    numberWords = len(stringList)
    lastWord = stringList[numberWords - 1]
    lastWordClean = string.replace(lastWord, '.', '', 1000)
    result = len(lastWordClean)
    #
    print(result)
    

lengthOfLastWord('testing how the string is split.')