import matplotlib.pyplot as plt
import numpy as np

print()
print("Plotting only the markers.")
xpoints = np.array([1, 12])
ypoints = np.array([2, 10])

#plt.plot(xpoints, ypoints, 'o')
#plt.show()
print()

print("Plotting multiple points.")
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
#plt.plot(xpoints, ypoints)
#plt.show()

#The default values for unspecified x values are (1, 2,3 4)
print("Using the default values of X")
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()