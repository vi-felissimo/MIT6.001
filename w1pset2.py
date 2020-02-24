while True:
    s = input("please input string:")
    foundB = 0
    sl = len(s) - 1
    i = 0
    while i < sl:
        if s[i:i+3] == "bob":
            foundB +=1
        i += 1
    print('Number of times bob occurs is:', foundB)
