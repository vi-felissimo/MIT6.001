import time

print('Please think of a number between 0 and 100!')
guess = 50
low = 0
high = 100

while True:
    print('Is your secret number', str(guess)+'?')
    reply = input("blabla:")
    start_time = time.time()
    if reply == 'h':
        high = guess
        guess = (low + guess)//2
        print("--- %.8f seconds ---" % (time.time() - start_time))
    elif reply == 'l':
        low = guess
        guess = (high + guess)//2
        print("--- %.8f seconds ---" % (time.time() - start_time))
    elif reply == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was:', guess)

    