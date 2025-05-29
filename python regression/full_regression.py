import matplotlib.pyplot as plt
"""
1. Class is the design of an object, it is a blueprint for creating objects.
2. Object is an instance of a class, it is a specific realization of the class.
3. Constructor is a special method that is called when an object is created, it initializes the object's attributes. In our case wee will be
fitting the car parts into the model. In Python the constructor is defined using the __init__ method.
4. __str__ is a special method that is called when the object is converted to a string, it is used to define the string representation of the object.

5. Abstraction is the process of hiding the implementation details and showing only the essential features of the object. In our case we are hiding the
6. Inheritance is the process of creating a new class that is based on an existing class, it allows us to reuse the code from the existing class.
Inheritance is redesign while maintaining backward compatibility.
7. Modularity is the process of breaking down a complex system into smaller, manageable parts. In our case we are breaking down the regression
 For modularity a project must capable of being stored in different failes.
 Files can be compiled independently and can be used in different projects.
 Files can be run and tested separately.
8. Polymorphism is the ability to define same commands for different contexts(Object) using the same symbol. "1" + "2" = "12" 
1+2=3
9. Interface is the position where 2 systems meet. Compatibility will be maintained by the interface.





"""


class RegressionPredict:
    def __init__(self, x, y,projecttitle):
        self.x = x
        self.y = y
        self.projecttitle=projecttitle
        self.n = len(x)
        self.sigmax = sum(x)
        self.sigmay = sum(y)
        self.x2 = [i*i for i in x]
        self.sigmax2 = sum([i*i for i in x])
        self.sigmay2 = sum([i*i for i in y])
        self.sigmaxy = sum([x[i]*y[i] for i in range(self.n)])
        self.b = (self.n * self.sigmaxy - self.sigmax * self.sigmay) / \
            (self.n * self.sigmax2 - self.sigmax2)
        self.a = (self.sigmay - self.b * self.sigmax) / self.n

        r = self.sigmaxy - (self.sigmax * self.sigmay / self.n)
        self.r = r / ((self.sigmax2 - (self.sigmax2 / self.n))
                      * (self.sigmay2 - (self.sigmay**2 / self.n)))**0.5

    def predict(self, x):
        return [self.a + self.b * xi for xi in x]

    def __str__(self):
        output = f"X = {self.x} \nY = {self.y}\nX2 = {self.x2} \nY2 = {self.sigmay2}\nXY = {self.sigmaxy}\n"
        return output

    def plot(self, digramtitle, plottitle, xlabel, ylabel):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(self.projecttitle)
        plt.grid(True)
        regressiondata = self.predict(self.x)
        plt.plot(self.x, self.y, color='red', label=digramtitle)
        plt.plot(self.x, regressiondata, color='green',
                 label="Line of Best Fit")

        predictruninput = [i for i in range(1, 9)]
        predictrunoutput = self.predict(predictruninput)
        regressiondata = self.predict(self.x)
        plt.plot(self.x, self.y, color='red', label=digramtitle)
        plt.plot(self.x, regressiondata, color='green',
                 label="Line of Best Fit")
        plt.plot(predictruninput, predictrunoutput,
                 color='yellow', label="Predicted Run")
        plt.legend()
        plt.show()
