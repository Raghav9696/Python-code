import cv2 as pp
pic =  pp.imread("torism_report.py/pics/amit.jpg")
print()
if pic is None:
    print("Picture not found")
else:
    print(type(pic))
    print(pic)
    output=pp.imshow("Show Picture", pic)
    print(output)
    output=pp.waitKey(0)
    print(output)