import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y = [2,3,4,5,6]
def plot_data(x, y):
    plt.scatter(x, y, color='blue', label='Data Points')
    plt.xlabel('Share Price')
    plt.ylabel('Y-axis')
    plt.title('basic plot')

    plt.grid(True)
    plt.plot(x, y, color='red', linestyle='-', label='Line of Best Fit')
    plt.legend()
    plt.show()
    plt.xlabel('x-axis')
    plt.ylabel('Y-axis')
    plt.plot(x, y, color='blue', label='Data Points')
    plt.title('basic plot')
    plt.legend()
    plt.grid(True)
    plt.scatter(x, y, color='red', label='Scatter Points') 

plt.show()
plot_data(x, y)