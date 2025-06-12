items = [("Pepsi", 10), ("Coke", 15)]
total = 0
for item in items:
    print(item, item[0], item[1])
    total += item[1]
print(total)
