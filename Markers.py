import matplotlib.pyplot as plt
import numpy as np

#Using marker() to emphasize the points being plotted.
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()

#using string formats marker|line|color
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints,'o:r')
plt.show()
#theres also '_' , '_,' , ':' , '__'

#setting the marker size
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms= 10)
plt.show()

#Setting the marker color 'mec'
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 5, mec = 'r', mfc = 'r')
plt.show()
#mfc - for color inside the marker. mfc = 'r'