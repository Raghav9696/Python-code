a=10
b=20
c=30
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print ("Equilateral Triangle")
    elif a==b or b==c or c==a:  
        print ("Isosceles Triangle")
    else:
        print ("scalene triangle")
else:
    print ("Not a triangle")