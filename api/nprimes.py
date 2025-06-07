n = 100
loopcount=0
primecount=0
for i in range(2,n+1):
    limit=i**.5
    limit=int(limit)
    isPrime=True
    for j in range (2,limit+1):
        loopcount+=1
        if i % j==0:
            isPrime=False
            break
    if isPrime:
        primecount+=1
        print(i,end=",")

print(f"\nloopcount={loopcount},primecount={primecount}",end=",")
    

