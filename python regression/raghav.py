import matplotlib.pyplot as plt
class RegressionPredict:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.sigmax = sum(x)
        self.sigmay = sum(y)
        self.x2 = [i*i for i in x]
        self.sigmax2 = sum([i*i for i in x])
        self.sigmay2 = sum([i*i for i in y])
        self.sigmaxy = sum([x[i]*y[i] for i in range(self.n)])
        self.b = (self.n * self.sigmaxy - self.sigmax * self.sigmay) / \
            (self.n * self.sigmax2 - self.sigmax**2)
        self.a = (self.sigmay - self.b * self.sigmax) / self.n

        r = self.sigmaxy - (self.sigmax * self.sigmay / self.n)
        self.r = r / ((self.sigmax2 - (self.sigmax**2 / self.n))
                      * (self.sigmay2 - (self.sigmay**2 / self.n)))**0.5

    def predict(self, x):
        return [self.a + self.b * xi for xi in x]

    def __str__(self):
        output = f"X = {self.x} \nY = {self.y}\nX2 = {self.x2} \nY2 = {self.sigmay2}\nXY = {self.sigmaxy}\n"
        return output

    def plot(self, digramtitle, plottitle, xlabel, ylabel):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(plottitle)
        plt.grid(True)
        regressiondata = self.predict(self.x)
        plt.plot(self.x, self.y, color='blue', label=digramtitle)
        plt.plot(self.x, regressiondata, color='blank',
                 label="Line of Best Fit")

        Youtubeinput = [i for i in range(1, 9)]
        predictYoutubeoutput = self.predict(Youtubeinput)
        regressiondata = self.predict(self.x)
        plt.plot(self.x, self.y, color='red', label=digramtitle)
        plt.plot(self.x, regressiondata, color='green',
                 label="Line of Best Fit")
        plt.plot(Youtubeinput, predictYoutubeoutput,
                 color='red', label="Predicted Youtube")
        plt.legend()
        plt.show()
