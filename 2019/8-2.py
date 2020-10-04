import numpy as np

if __name__ == "__main__":
    line = input()

    line = [int(x) for x in line]
    arr = np.array(line)

    arr = arr.reshape((-1, 6, 25))

    layer = np.argmin(np.count_nonzero(arr == 0, axis=(1, 2)))

    ones = np.count_nonzero(arr[layer, :, :] == 1)
    twos = np.count_nonzero(arr[layer, :, :] == 2)

    vals = np.argmax(arr != 2, axis=0)

    for i in range(0, vals.shape[0]):
        for j in range(0, vals.shape[1]):
            if arr[vals[i, j], i, j] == 0:
                print(" ", end="")
            else:
                print("X", end="")
        print()



