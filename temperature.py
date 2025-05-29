import matplotlib.pyplot as plt

def plot_data(x, y):
    # plt.scatter(x, y, label='Data Points')
    # plt.fill_between(x, y, color='lightblue', alpha=0.5, label='Area Under Curve')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Humidity (%)')
    plt.title('Temperature and  Humidity in varanasi')
    plt.grid(True)
    plt.plot(x, y, color='red', linestyle='-', label='Line of Best Fit')
    plt.legend()
    plt.show()


x = [1,2,3,4,5,6,7]

y = [28, 29, 32, 28, 29, 30, 33]

plot_data(x, y)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
