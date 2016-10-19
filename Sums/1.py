import time

def sum_of_n(n):
    start = time.time()

    thesum = 0
    for i in range(1, n + 1):
        thesum += i
    end = time.time()
    return thesum, end - start

for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_n(1000))
