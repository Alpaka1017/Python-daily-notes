import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# You might need to install pandas and/or pyplot into your python, just look up how to do that

# Put your file in the same folder as this file and change the 'FILENAME' to the name of your file
df = pd.read_csv("campbelldiagramm.csv")

npA = df.to_numpy()
print(npA.shape)

def colZip(A):
    cols = []
    for n in range(len(A[0])): # 6 cols
        colArr = []
        for m in range(len(A)): # 9 rows
            colArr.append(A[m][n])
        cols.append(colArr)

    return cols

#print(len(npA))

npCols = colZip(npA)
print(npCols, np.shape(npCols))
# Plotting variable 5 and 6 (Change to (1 - the column you want)) aka: A in excel = 0 in here, B=1, C=2, etc.

plt.plot(npCols[2], npCols[3])
plt.plot(npCols[2], npCols[4])
plt.plot(npCols[2], npCols[5])

# if npCols[1] == “1,”:
# plt.plot(npCols[2], npCols[3])
# Copy paste that line if you need more columns


# Edit these to the things you want: (If you added or removed variables, just make the legend larger/smaller with commas)
plt.xlabel("Nodal Diameter")
plt.ylabel("Frequency")
plt.legend(["Mode 1", "Mode 2", "Mode 3"])

# Modify the appearance of axis
'''plt.xlim(0, 8)
plt.ylim(0, 4000)
plt.xticks(range(9))
plt.yticks(range(0, 4001, 500))'''

plt.grid()
plt.show()
