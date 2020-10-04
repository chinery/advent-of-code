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
    maxpower = 0
    for size in range(1, 61):
        print("Size {}".format(size))
        sums = signal.convolve2d(grid, np.ones((size, size)), mode="same")
        coords = np.unravel_index(np.argmax(sums, axis=None), sums.shape)
        if sums[coords] > maxpower:
            maxpower = sums[coords]
            if size % 2 == 0:
                offset = size/2
            else:
                offset = (size-1)/2
            maxcoords = (coords[1]-offset+1, coords[0]-offset+1, size)

    print(maxcoords)