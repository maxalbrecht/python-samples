def romanToInt(string):
    """
    The following takes a roman numeral as a string and converts it to an int
    """
    Mappings = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    currentNumeralIndex = len(string) - 1
    while currentNumeralIndex >= 0:
        if currentNumeralIndex == len(string) - 1:
            result += Mappings[string[currentNumeralIndex]]
        if currentNumeralIndex < len(string) - 1:
            if Mappings[string[currentNumeralIndex]] >= Mappings[string[currentNumeralIndex + 1]]:
                result += Mappings[string[currentNumeralIndex]]
            if Mappings[string[currentNumeralIndex]] < Mappings[string[currentNumeralIndex + 1]]:
                result -= Mappings[string[currentNumeralIndex]]
        currentNumeralIndex -= 1
    print(result)
    
#romanToInt('CDXXVII')
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    