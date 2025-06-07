n = 500
loopcount = 0
primecount = 1
print(2, end=",")
for i in range(3, n+1, 2):
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
