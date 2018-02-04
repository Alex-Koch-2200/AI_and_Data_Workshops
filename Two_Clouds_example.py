import random
import numpy as np
import matplotlib.pyplot as plt

data_x = np.zeros([100])
data_y = np.zeros([100])

for i in range(0,50):
    data_x[i] = random.gauss(35,5)
    data_y[i] = random.gauss(65,5)

for i in range(50,100):
    data_x[i] = random.gauss(65,5)
    data_y[i] = random.gauss(35,5)

plt.scatter(data_x, data_y)
plt.show()

