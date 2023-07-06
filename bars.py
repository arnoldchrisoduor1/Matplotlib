import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([5, 8, 10, 9])
plt.bar(x, y, width = 0.3)
plt.show()

#Creating horizontal bars.
x = np.array(["A", "B", "C", "D"])
y = np.array([5, 8, 10, 9])
plt.barh(x, y, color = 'red', height=0.3)
plt.show()