def fac(n):
    intNum = []
    ## check if n can be divided by i
    for i in range(1, n):
        if (n % i == 0):
                intNum.append(i)
    return intNum

#list store all fac sums
def listSum(n):
    d = {}
    for i in range(1, n+1):
        d[i] = sum(fac(i))        
    return d
    
n = int(input('Enter a number: '))
ResultDict = listSum(n)
for k,v in ResultDict.items():
    #if ResultDict[k] == ResultDict[v]:
    #print('Same.', k , v)
    if k != v:
        try:
            if k == ResultDict[v]:
                print(k, '-', v)
                continue
        except:
            continue
