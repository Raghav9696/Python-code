from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy
from numpy.polynomial import polynomial as poly
deg = 2
actualx = [1, 2, 3, 4, 5, 6]
actualy = [1, 4, 9, 16, 25, 33]


def bestfitModel(x, y):
    bestcoeff = 0
    bestmodel = None
    bestpower = 0
    for r in range(1, 6):
        model = numpy.poly1d(numpy.polyfit(x, y, r))
        coeff = r2_score(y, model(x))
        if coeff > bestcoeff:
            bestcoeff = coeff
            bestmodel = model
            bestpower = r
    return bestcoeff, bestmodel, bestpower


x = [40, 70, 50, 60, 80, 50, 90, 40, 60, 60]

listy = [[2.5, 6.0, 4.5, 5.0, 4.5, 2.0, 5.5, 3.0, 4.5, 3.0]]
y = listy[0]
deg = 1
npp = numpy.polyfit(x, y, deg)
model = numpy.poly1d(npp)
coeff = r2_score(y, model(x))

print(f'\ndeg={deg}\nx={x}\ny={y}\nEquation={model}\nCorrelation={coeff}')
predictx = 0
result = model(predictx)
print(f'\nresult={result}\tfor x={predictx}')
outputy = [model(i) for i in x]
plt.scatter(x, y)
plt.plot(x, y)
plt.plot(x, y)
plt.scatter(x, outputy)
plt.title("Multiple Degree Regression")
plt.legend()
plt.show()

equation = poly.Polynomial.fit(actualx, actualy, deg=deg)
print(equation)
