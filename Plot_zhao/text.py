import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# from scipy.optimize import curve_fit, fsolve

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

    # Define Speed Line
    xSp = [n for n in range(17)]
    ySp = [n * 16000 / 60 for n in xSp]
    xSp = [n for n in range(9)] + [7 - n for n in range(8)]

    print(len(xSp),len(ySp))
    print(len(x),len(y3))

    for i in range(len(x) - 1):
        if y1[i] <= ySp[i-9] and y1[i + 1] >= ySp[i - 8] or y1[i] >= ySp[i - 9] and y1[i + 1] <= ySp[i - 8]:
            x_inter = (ySp[i - 9] - y1[i] + x[i] * (y1[i + 1] - y1[i]) / (y1[i + 1] - y1[i]) - xSp[i - 9] * (ySp[i - 8] - ySp[i - 9]) / (
                        y1[i + 1] - y1[i])) * (y1[i + 1] - y1[i]) / (ySp[i - 8] - y1[i + 1])
            y_inter = y1[i] + (y1[i + 1] - y1[i]) * (x - x1[i]) / (x1[i + 1] - x1[i])
            break

            print(x_inter,y_inter)
    # Define fitting interval
    '''xSp_fit_1 = xSp[3:4]
    xSp_fit_2 = xSp[6:7]
    xSp_fit_3 = xSp[7:8]

    ySp_fit_1 = ySp[3:4]
    ySp_fit_2 = ySp[6:7]
    ySp_fit_3 = ySp[7:8]

    x1_fit = x[3:4]
    x2_fit = x[6:7]
    x3_fit = x[7:8]
    print(x3_fit)
    print(xSp_fit_3)

    y1_fit = y1[3:4]
    y2_fit = y1[6:7]
    y3_fit = y1[7:8]

    # Curve fitting
    fit_Sp_1, _ = np.polyfit(xSp_fit_1, ySp_fit_1, 1)
    fit_Sp_2, _ = np.polyfit(xSp_fit_2, ySp_fit_2, 1)
    fit_Sp_3, _ = np.polyfit(xSp_fit_3, ySp_fit_3, 1)

    fit_y1 = np.polyfit(x1_fit, y1_fit, 1)
    fit_y2 = np.polyfit(x2_fit, y2_fit, 1)
    fit_y3 = np.polyfit(x3_fit, y3_fit, 1)

    plt.plot()
    # Calculate intersection
    diff_func_1 = np.poly1d(fit_Sp_1) - np.poly1d(fit_y1)
    diff_func_2 = np.poly1d(fit_Sp_2) - np.poly1d(fit_y2)
    diff_func_3 = np.poly1d(fit_Sp_3) - np.poly1d(fit_y3)

    # Resolve the coordinate
    roots_1 = np.roots(diff_func_1)
    roots_2 = np.roots(diff_func_2)
    roots_3 = np.roots(diff_func_3)
    print(roots_1)
    print(roots_2)
    print(roots_3)'''

    '''# x
    for root_1 in roots_1:
        if np.isreal(root_1):
            root_real_1 = np.real_if_close(root_1)
    for root_2 in roots_2:
        if np.isreal(root_2):
            root_real_2 = np.real_if_close(root_2)
    for root_3 in roots_3:
        if np.isreal(root_3):
            root_real_3 = np.real_if_close(root_3)

    # y
    y_real_1 = (np.polyval(fit_y1, root_real_1) + np.polyval(fit_Sp, root_real_1)) / 2.0
    y_real_2 = (np.polyval(fit_y2, root_real_2) + np.polyval(fit_Sp, root_real_2)) / 2.0
    y_real_3 = (np.polyval(fit_y3, root_real_3) + np.polyval(fit_Sp, root_real_3)) / 2.0

    print(root_real_1)
    print(root_real_2)
    print(root_real_3)
    # print(np.isreal(roots_1))
    print(type(roots_1))
    # print(np.isreal(roots_2))
    print(type(roots_2))
    # print(np.isreal(roots_3))
    print(type(roots_3))
    print(y_real_1)
    print(y_real_2)
    print(y_real_3)'''

    # plot
    plt.plot(x, y1, label='Mode1')
    plt.plot(x, y2, label='Mode2')
    plt.plot(x, y3, label='Mode3')

    # Modify scale of axis and interval
    # plt.xlim(0, 8)
    # plt.ylim(0, 4000)
    # plt.xticks(range(9))
    # plt.yticks(range(0, 4001, 500))

    plt.plot(xSp, ySp, 'red', label='16k RPM (Speed Line)')

    # Set legend
    plt.xlabel("Nodal Diameter")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid()
    plt.title('ZZENF diagram')

    # Notation
    '''plt.annotate('Intersection 1', xy=(root_real_1, y_real_1), xytext=(root_real_1 + 0.1, y_real_1 + 10),
                 arrowprops=dict(facecolor='red', shrink=0.05))
    plt.annotate('Intersection 2', xy=(root_real_2, y_real_2), xytext=(root_real_2 + 0.1, y_real_2 + 10),
                 arrowprops=dict(facecolor='red', shrink=0.05))
    plt.annotate('Intersection 3', xy=(root_real_3, y_real_3), xytext=(root_real_3 + 0.1, y_real_3 + 10),
                 arrowprops=dict(facecolor='red', shrink=0.05))'''
    # Show the plot
    plt.show()


if __name__ == '__main__':
    arr_plot()
