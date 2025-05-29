a = 1
b = 2
c = 3
mid = (a if a >= b else b) if a >= c else (b if b >= c else c)
print(mid)
