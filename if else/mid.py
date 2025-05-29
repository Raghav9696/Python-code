a = 2
b = 1
c = 3
if (a >= b and a <= c) or (a >= c and a <= b):
    mid = a
elif (b >= a and b <= c) or (b >= c and b <= a):
    mid = b
else:
    mid = c
print(mid)
print ("it is a mid of three numbers ")