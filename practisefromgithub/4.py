year = 2024
month = 2
if year < 1:
    print("Invalid year")
elif month < 1 or month > 12:
    print("Invalid month")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("29 days")
    else:
        print("28 days")
