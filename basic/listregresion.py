import matplotlib.pyplot as plt



def plot_data(x, y,x2,label,title):
    plt.scatter(x, y, color='blue', label=label)
    plt.xlabel('Share Price')
    plt.ylabel('Y-axis')
    plt.title(title)

    plt.grid(True)
    plt.plot(x, y, color='red', linestyle='-', label="X-Y")
    plt.plot(x, x2, color='green', linestyle='-', label="X-X2")
    plt.legend()
    plt.show()



x = [1, 2, 3, 4, 5]
y = [2, 3, 5,4,  6]
print(x, y)
x2 = [i*i for i in x]
y2 = [i*i for i in y]
n = len(x)
xy = [x[i]*y[i] for i in range(n)]
print(x2, y2, xy)
sigmax= sum(x)
print("sigmax:", sigmax)
sigmay = sum(y)
print("sigmay:", sigmay)
sigmax2 = sum(x2)
print("sigmax2:", sigmax2)
sigmay2 = sum(y2)
print("sigmay2:", sigmay2)
sigmaxy = sum(xy)
print("sigmaxy:", sigmaxy)

b = (n*sigmaxy - sigmax*sigmay) / (n*sigmax2 - sigmax**2)
a = (sigmay- b*sigmax)/n

print("a:", a)
print("b:", b)
plot_data(x,x2, xy,"X-Y","Lines of Regression")

