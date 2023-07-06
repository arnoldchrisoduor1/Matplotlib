import matplotlib.pyplot as plt
import numpy as np

#Leblling the axes.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)
# plt.title("Sports watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie burnage")
# plt.show()

#Setting fonts.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'red', 'size':15}

plt.title("Sports Data", fontdict=font1, loc = 'left')
plt.xlabel("Pulse rate", fontdict=font2)
plt.ylabel("Calorie burnage", fontdict=font2)
plt.plot(x, y)
plt.show()

