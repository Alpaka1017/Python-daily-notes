import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("campbelldiagramm.csv")
npA = df.to_numpy()


def data_extract(arr_2dim):
    if not isinstance(arr_2dim, np.ndarray):
        raise TypeError("Input must be a NumPy array")
    elif arr_2dim.shape[1] < 6:
        raise IndexError("Input must have at least 6 columns")

    arr_2dim = np.char.replace(arr_2dim.astype(str), ',', '.')
    x = arr_2dim[:, 2].astype(float)
    y_mode1 = arr_2dim[:, 3].astype(float)
    y_mode2 = arr_2dim[:, 4].astype(float)
    y_mode3 = arr_2dim[:, 5].astype(float)

    return x, y_mode1, y_mode2, y_mode3


def arr_plot():
    x, y1, y2, y3 = data_extract(npA)
    # plot
    plt.plot(x, y1, label='Mode1')
    plt.plot(x, y2, label='Mode2')
    plt.plot(x, y3, label='Mode3')

    # Modify scale of axis and interval
    plt.xlim(0, 8)
    plt.ylim(0, 4000)
    plt.xticks(range(9))
    plt.yticks(range(0, 4001, 500))

    # Set legend
    plt.legend()
    plt.title('Campbell Diagram')

    # Show the plot
    plt.show()


if __name__ == '__main__':
    arr_plot()