def isPalindrome(string):
    isAPalindrome = True
    length = len(string)
    currentIndex = 0
    while currentIndex <= (length/2) - 1 and isAPalindrome == True:
        if string[currentIndex] != string[length - currentIndex - 1]:
            isAPalindrome = False
        currentIndex += 1
    print(isAPalindrome)

isPalindrome('test')        