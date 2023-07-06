import matplotlib.pyplot as plt
import numpy as np

# y = np.array([35, 25, 25, 15,])
# mylabels = ["Cherry", "Apples", "Bananas", "Mangoes"]
# myexlode = [0.2, 0, 0, 0]
# plt.pie(y, labels = mylabels, startangle=90, explode=myexlode, shadow=True)
# plt.show()

#Specifying the colors.
y = np.array([35, 25, 25, 15,])
mylabels = ["Cherry", "Apples", "Bananas", "Mangoes"]
myexlode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, startangle=90, explode=myexlode, shadow=True, colors=mycolors)
plt.legend(title="Four Fruits")
plt.show()