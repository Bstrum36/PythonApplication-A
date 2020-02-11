from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.plot(x, np.sin(x), 'b')
    plt.plot(x, (np.cos(x)+np.sin(x)), 'g')
    plt.plot(x, (np.cos(x)-np.sin(x)), 'r')

    plt.show()

main()