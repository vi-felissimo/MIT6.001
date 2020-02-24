''' calculate FIXED monthly paidment to paid off balance in a year
2 variables: 
    balance; annualInterestRate
using binary search to get 2 decimal number accuracy
'''
import time

def fixM2(balance, AIR, j=0):
    # start from next 10th number after balance/12
    minP = ((balance/12)//10 + 1) * 10
    # balance/12 < paidment < balance * (1+interest rate%) 
    maxP = balance * (1+AIR) / 12
    ppay = (minP + maxP)/2
    while True:
        # calculate total year balance TYB
        yearTl = balance
        remaining = balance
        for i in range(12):      
            remaining = remaining - ppay
            #calculate this month's interest
            interestM = remaining * (AIR/12)
            remaining += interestM
            yearTl += interestM
            i += 1
        # pay total
        ppayYear = ppay * 12
        # check pay totoal and yeartl
        if abs(ppayYear - yearTl) < 0.01:
            return ppay, ppayYear - balance, j
        elif ppayYear > yearTl:
            maxP = ppay
        else:
            minP = ppay
        # update pay per month
        ppay = (minP + maxP)/2
        j += 1

while True:
    numstr = input('Balance? Annual Interest Rate?\n')
    numStrArray = numstr.split()
    testBalance = float(numStrArray[0])
    testAIR = float(numStrArray[1])
    startT = time.time()
    result = fixM2(testBalance,testAIR)
    print('--- pay %0.2f monthly to pay off.---' % result[0])
    print ('----- %.5f s to calculate-----' % (time.time()-startT))
    print('---------paid %.2f more.----------'% result[1])
    print(result[2], 'times')
