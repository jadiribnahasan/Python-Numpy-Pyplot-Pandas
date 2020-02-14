import matplotlib.pyplot as plt
import random as rand
import numpy as np

print(plt.style.available)
plt.style.use('seaborn')


def RunSim(goal, trials):

    totalHit = 0

    for i in range(trials):
        d1 = int(rand.uniform(1, 6))
        d2 = int(rand.uniform(1, 6))
        d3 = int(rand.uniform(1, 6))
        d4 = int(rand.uniform(1, 6))
        d5 = int(rand.uniform(1, 6))
        st = f'{d1}{d2}{d3}{d4}{d5}'
        if st == goal:
            totalHit += 1

    return float((totalHit/trials))


if __name__ == '__main__':

    trials_x = np.arange(1, 101)
    error_y = []
    for i in range(1, 101):
        error_y.append(abs(RunSim('11111', i) - (1/6**5)))

    plt.bar(trials_x, error_y)
    #plt.plot(trials_x , error_y)

plt.tight_layout()
plt.show()
