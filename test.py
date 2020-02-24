def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #compare char and the middle char of aStr
    cpChar = len(aStr)//2
    if len(aStr)==1:
        return char == aStr[0]
    elif len(aStr) == 0:
        return False
    elif char > aStr[cpChar]:
        return isIn(char, aStr[cpChar:])
    elif char == aStr[cpChar]:
        return True
    else:
        return isIn(char, aStr[:cpChar])
    
