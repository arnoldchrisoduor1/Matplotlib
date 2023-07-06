import matplotlib.pyplot as plt
import numpy as np

#generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10.
x = np.random.normal(70, 10, 250)
plt.hist(x)
plt.show()