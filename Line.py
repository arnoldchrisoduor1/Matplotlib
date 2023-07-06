import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()

#Line style can aslo be dashed, 

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, ls = '--')
plt.show()

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color = 'r', ls = '--')
plt.show()

#Using linewidth
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '10')
plt.show()

#Plotting multiple lines.
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()

#Specifying the x and y values for two lines.
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()