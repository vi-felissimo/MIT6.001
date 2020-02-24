def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''  
    numList = []
    for a in aDict.values():
        numList.append(len(a))
    if numList == []:
        return
    most = max(numList)
    for k in aDict.keys():
        if len(aDict[k]) == most:
            return k

animals = {}

print(biggest(animals))