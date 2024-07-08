import numpy as np
import matplotlib.pyplot as plt

def randomwalk2D(n):
    x = np.zeros(n)
    y = np.zeros(n)
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    for i in range(1, n):
        step = np.random.choice(directions)

        if step == "RIGHT":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif step == "LEFT":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif step == "UP":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        elif step == "DOWN":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1

    return x, y

x, y = randomwalk2D(1000)
plt.plot(x, y)
plt.show()
