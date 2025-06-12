places = [
    ("Srinagar", 5000),
    ("Sarnath", 2000),
    ("Sankat Mouchan", 1500),
    ("Dashashwamedh Ghat", 1000),
    ("Banaras Hindu University (BHU) & Bharat Kala Bhavan", 2500)
]
chosenplaces=[]
while True:
    print("\n (0)-Exit, (1)--Choose location , (2)-Print , (3)--Complete Booking ")

    option = int(input("Choose option (0),(1),(2) or (3)--\n"))
    if option == 0:
        break
    if option == 1:
        print("Choose location")
        print(places)
        location = int(input("Enter location1"))-1
        if places[location] in chosenplaces:
            print("Already chosen")
        else:
            chosenplaces.append(places[location])
        continue
    if option == 2:
        print("Chosen places")
        print(chosenplaces)
        continue
    if option == 3:
        man_details = {
            "Name": (input("Enter Your Name")),
            "Phone_No": input("Enter your phone number--:"),
            "address": input("Enter your address(local address)--:"),
            "places": chosenplaces}
        totalcost = 0
        for tpl in chosenplaces:
            totalcost = totalcost + tpl[1]
        print(totalcost)
        print(man_details)
        break
