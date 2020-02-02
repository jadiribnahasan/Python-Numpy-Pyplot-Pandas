from matplotlib import pyplot as plt
import numpy as np
import math as math
import random as rand


def monteCarloPi(trials, radius):
    hits = 0
    for i in range(trials):
        xr = rand.uniform(0, radius)
        yr = rand.uniform(0, radius)
        distance = math.sqrt(xr**2 + yr**2)
        if(distance <= radius):
            hits += 1
            plt.plot(xr, yr, 'go')
        else:
            plt.plot(xr, yr, 'ro')

    pi = (hits/trials)*4
    print(pi)

    xv = np.linspace(0, radius, 100)
    yv = np.sqrt(radius**2 - xv**2)

    plt.plot(xv, yv)
    plt.title(f'pi = {pi}')
    plt.show()


monteCarloPi(1000, 2.5)  # Increase trials for accurate value of pi
