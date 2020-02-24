''' calculate credit card balance after one year 
if one only paid min monthly.
3 variables: 
    balance; annualInterestRate; monthlyPaymentRate;
'''

def yearUnpaid(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        # calculate unpaid balance
        balance *= (1 - monthlyPaymentRate)
        # calculate interest of the month
        interest = (balance) * annualInterestRate/12
        # unpaid = remaining this month + interest
        balance = balance + interest
        #print('month %d-UnpaidBalance: %.2f.' % (i+1, balance))
        i += 1
    return balance

while True:
    numstr = input('Balance? Annual Interest Rate? Minimin paidment?\n')
    numStrArray = numstr.split()
    numArray = []
    for n in numStrArray:
        l = float(n)
        numArray.append(l)
    print('Remaining balance: %.2f' % \
        yearUnpaid(numArray[0], numArray[1], numArray[2]))