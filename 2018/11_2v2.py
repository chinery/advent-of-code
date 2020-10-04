# v1 worked but was slow, think I can do better...
# this one uses a 2D prefix sum array instead of convolution
#
# the cool thing is that this one speeds up as the size gets
# bigger, rather than slowing down

import numpy as np
from scipy import signal


class TwoDPrefixSumArray:
    def __init__(self, contents):
        self.array = np.zeros(contents.shape)
        self.populate(contents)

    def populate(self, contents):
        for i in range(0, contents.shape[0]):
            for j in range(0, contents.shape[1]):
                if i == 0 and j == 0:
                    self.array[i, j] = contents[i, j]
                elif i == 0:
                    self.array[i, j] = self.array[i, j-1] + contents[i, j]
                elif j == 0:
                    self.array[i, j] = self.array[i-1, j] + contents[i, j]
                else:
                    self.array[i, j] = self.array[i-1, j] \
                                       + self.array[i, j-1] \
                                       - self.array[i-1, j-1] + contents[i, j]

    def sum_region(self, x, y, size):
        imin = y-1
        jmin = x-1
        imax = imin + size - 1
        jmax = jmin + size - 1
        total = self.array[imax, jmax]

        if imin > 0 and jmin > 0:
            total = total - self.array[imin-1, jmax] \
                - self.array[imax, jmin-1] + self.array[imin-1, jmin-1]
        elif imin > 0:
            total -= self.array[imin-1, jmax]
        elif jmin > 0:
            total -= self.array[imax, jmin-1]

        return total


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

    # convert grid to prefix sum array
    psa = TwoDPrefixSumArray(grid)

    maxpower = 0
    for size in range(1, 301):
        print("Size {}".format(size))
        for y in range(1, 301-size+1):
            for x in range(1, 301-size+1):
                power = psa.sum_region(x, y, size)
                if power > maxpower:
                    maxpower = power
                    maxcoords = (x, y, size)

    print(maxcoords)