from numpy.polynomial import polynomial as poly
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np
import random
import math

deg=1


#Linear Input

actualx =[1,2,3,4]#
# actualy=[2*x - 4 for x in actualx]# y=2*x + 4

actualy=[5,12,54,87]
equation=poly.Polynomial.fit(actualx,actualy,deg=deg).convert()
# Equation based on the input data
print("y=",equation)
x=1
result = 28.8*x -32.5
print(result)


#Print the generated equationprint(actualx)print(actualy)predictionx=np.linspace(1,10,10
# values from 1 to 10. Predicted values input


