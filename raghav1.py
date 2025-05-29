import matplotlib.pyplot as plt
def plot_data(x, y, a=None, b=None):
    plt.scatter(x, y, color='blue', label='Data Points')
    plt.xlabel('Share Price')
    plt.ylabel('Price')
    plt.title('Scatter Plot of Data Points')
    plt.grid(True)
    if a is not None and b is not None:
        # Plot regression line
        y_fit = [a + b * xi for xi in x]
        plt.plot(x, y_fit, color='green', linestyle='-', label='Line of Best Fit')
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
# Plot with regression line
plot_data(x, y, a, b)

# Optionally, plot the squared data if needed
# plot_data(x2, y2)
plot_data(x, y)
plot_data(x, y)