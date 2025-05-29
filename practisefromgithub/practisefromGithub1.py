# to find the max of three numbers are following :
a = 1
b = 2
c = 3
max = a if a >= b else b
max = (a if a >= c else c)if a >= b else (b if b >= c else c)
print(max)
