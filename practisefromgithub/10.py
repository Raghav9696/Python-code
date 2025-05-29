a = 1
b = 2
c = 3
d =4
max = a if a >= b else b
max = (a if a >= c else c)if a >= b else (b if b >= c else c)
max = (a if a >= d else d)if a >= b else (b if b >= c else c)
print(max)   