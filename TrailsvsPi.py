

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

    pi = (hits/trials)*4

    return pi


for x in range(1, 1000):
    d = ((3.14159-monteCarloPi(x, 2.5)))
    xp = [x]*20
    yp = np.linspace(0, d, 20)
    plt.plot(xp, yp)

plt.show()
