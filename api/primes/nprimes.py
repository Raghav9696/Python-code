n = 500
loopcount = 0
primecount = 3
print(2, end=",")
print(3, end=",")
print(5, end=",")
t=2
i=5
while i<n-1:
    i+=t
    t=6-t
    # print(i)
    # input()
    limit = i**.5
    limit = int(limit)
    isPrime = True
    for j in range(3, limit+1, 2):

        loopcount += 1
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primecount += 1
        print(i, end=",")

print(f"\nloopcount={loopcount},primecount={primecount}", end=",")
