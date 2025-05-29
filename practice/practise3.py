a = 100
b = 200
c = 50
min = a if a <= b else b
min = (a if a <= c else c) if a <= b else (b if b <= c else c)
print(min)