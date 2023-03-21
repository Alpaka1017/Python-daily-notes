import time
import numpy

start_time = time.time()

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

end_time = time.time()

elapsed_time = end_time - start_time

print("程序运行时间为：{:.16f}秒".format(elapsed_time))




