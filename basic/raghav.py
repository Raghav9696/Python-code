import matplotlib.pyplot as plt


def plot_data(x, y):
    plt.scatter(x, y, color='blue', label='Data Points')
    plt.xlabel('Share Price')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of Data Points')

    plt.grid(True)
    plt.plot(x, y, color='red', linestyle='-', label='Line of Best Fit')
    plt.legend()
    plt.show()


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 6]

plot_data(x, y)
