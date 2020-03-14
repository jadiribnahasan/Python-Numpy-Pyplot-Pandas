import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

N = 100
vals = [0, 1]
grid = np.random.choice(vals, N*N, p=[0.8, 0.2]).reshape(N, N)


def countLive(pos):
    moves = [[0, -1], [-1, 0], [1, 1], [-1, -1],
             [-1, 1], [1, -1], [1, 0], [0, 1]]
    count = 0

    for i in range(0, 8):
        pos0 = pos[0] + moves[i][0]
        pos1 = pos[1] + moves[i][1]
        if pos0 >= 0 and pos0 < N and pos1 >= 0 and pos1 < N:
            if grid[pos0][pos1] == 1:
                count += 1
    return count


def generate(data):
    global grid
    nextGrid = grid.copy()

    for i in range(N):
        for j in range(N):
            livecount = countLive([i, j])

            if grid[i, j] == 1:
                if (livecount < 2) or (livecount > 3):
                    nextGrid[i, j] = 0
            else:
                if livecount == 3:
                    nextGrid[i, j] = 1
    grid = nextGrid
    mat.set_data(nextGrid)
    return mat


fig, ax = plt.subplots()

mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, generate, interval=50, save_count=50)

plt.show()
