import math

def circle_calculator():
    print ("Welcome to circle calculator")
    print("Choose what you want to calculate:")
    print("1. Area")
    print("2. Circumference")
    print("3. Diameter")
    print("4. Arc Length")
    print("5. Sector Area")
    print("6. Chord Length")

    choice = int(input("Enter your choice (1-6): "))
    r = float(input("Enter the radius of the circle: "))

    if choice == 1:
        area = math.pi * r**2
        print("Area =", round(area, 2))

    elif choice == 2:
        circumference = 2 * math.pi * r
        print("Circumference =", round(circumference, 2))

    elif choice == 3:
        diameter = 2 * r
        print("Diameter =", diameter)

    elif choice == 4:
        angle = float(input("Enter the angle in degrees: "))
        arc_length = (angle / 360) * 2 * math.pi * r
        print("Arc Length =", round(arc_length, 2))

    elif choice == 5:
        angle = float(input("Enter the angle in degrees: "))
        sector_area = (angle / 360) * math.pi * r**2
        print("Sector Area =", round(sector_area, 2))

    elif choice == 6:
        angle = float(input("Enter the angle in degrees: "))
        angle_rad = math.radians(angle)
        chord_length = 2 * r * math.sin(angle_rad / 2)
        print("Chord Length =", round(chord_length, 2))

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
       