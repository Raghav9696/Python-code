# to find the leap year are following :
year = 2014
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:    
    print("not a leap year")
