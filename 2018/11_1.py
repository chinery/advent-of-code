import numpy as np
from scipy import signal

if __name__ == "__main__":
    try:
        while True:
            line = input()
            serial = int(line)
    except EOFError:
        pass

    # X coordinates plus 10
    rack = np.tile(np.arange(11, 312), (300, 1))
    # multiply by Y coordinates
    grid = rack * np.arange(1, 301).reshape((300, 1))
    # add serial number
    grid += serial
    # multiply by x plus 10 again
    grid *= rack
    # keep only the hundreds digit
    grid = (grid // 100) % 10
    # subtract 5
    grid -= 5

    # print(grid[195, 216])

    # find maximum in 3x3 window
    sums = signal.convolve2d(grid, np.ones((3, 3)), mode="same")
    maxcoords = np.unravel_index(np.argmax(sums, axis=None), sums.shape)
    print(maxcoords[1], maxcoords[0])
