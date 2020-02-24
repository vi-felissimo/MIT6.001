''' calculate FIXED monthly paidment to paid off balance in a year
2 variables: 
    balance; annualInterestRate
'''

def fixedM(balance, AIR):
    # start from next 10th number after balance/12
    ppay = ((balance/12)//10 + 1) * 10
    # balance/12 < paidment < balance * (1+interest rate%) 
    maxIts = balance * (1+AIR) / 12
    while ppay < maxIts:
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
        # check if paid off
        if yearTl <= ppay * 12:
            return ppay
        ppay += 10

while True:
    numstr = input('Balance? Annual Interest Rate?\n')
    numStrArray = numstr.split()
    testBalance = float(numStrArray[0])
    testAIR = float(numStrArray[1])
    print('--- pay %d monthly to pay off.---' % fixedM(testBalance,testAIR))

