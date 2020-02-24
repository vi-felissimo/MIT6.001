# find the longest alphabetical substring in s
s = input("enter a string pls:")
CountS = 0
LCount = 1
starti = 0
i = 1
ls = len(s)
while i < ls:
    #print(s[i], ord(s[i]))
    if ord(s[i-1]) <= ord(s[i]):
        CountS += 1
        if CountS > LCount:
            LCount = CountS
            starti = i - LCount
            #print("longer:", s[i], LCount)
    else:
        CountS = 0
    i += 1
print("Longest substring in alphabetical order is:", \
    s[starti:starti+LCount+1])

# other solutions in p1,p2 
print("Number of vowels:", str(len([i for i in s if i \
    in "aeiou"])))

print("here:", [i for i in s if i \
    in "aeiou"])

print("Number of times bob occurs is:", str(len([i for \
    i in range(len(s) - 2) if s[i:i + 3] == "bob"])))

print('Number of vowels:', sum(c in 'aeiou' for c in s))

print('Number of times bob occurs is:', sum(s[i:i+3] == 'bob'\
    for i in range(len(s))))
