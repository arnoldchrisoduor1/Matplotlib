import matplotlib.pyplot as plt
import numpy as np

#Plotting Grid lines
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif', 'color':'green', 'size': 15}
font2 = {'family':'serif', 'color':'blue', 'size': 20}

plt.title("Sports Data", fontdict=font2)
plt.xlabel("Pulse Rate", fontdict=font1)
plt.ylabel("Calorie Burnage", fontdict=font1)
plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

#specifying the grid lines to display.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif', 'color':'green', 'size': 15}
font2 = {'family':'serif', 'color':'blue', 'size': 20}

plt.title("Sports Data", fontdict=font2)
plt.xlabel("Pulse Rate", fontdict=font1)
plt.ylabel("Calorie Burnage", fontdict=font1)
plt.plot(x, y)
plt.grid(axis = 'x')
plt.show()

