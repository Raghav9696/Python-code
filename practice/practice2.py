# to find the the max of three numbers ::
a = 100
b = 20
c = 30
max = a if a >= b else b
max = (a if a >= c else c) if a >= b else (b if b >= c else c)
print(max)