'''
Alex Koch
AI and Data Workshops 2018
MANSEDS (Manchester Students for the Exploration and Development of Space) 
http://manseds.co.uk

Descripton: Data set of 2 spirals with added Gaussian random noise
Exercise: Classify the data points according to which spiral they belong to and output
          this classification in an appropriate manner. 

An example solution(s) is provided in a separate file
'''

import random
import numpy as np
import matplotlib.pyplot as plt

data_points = 400 #  increasing this number creates a more densely packed spiral in terms of data points per revolution
N = int(data_points / 2) # number of points per set

data_x = np.zeros([data_points])
data_y = np.zeros([data_points])
labels = [] # This will contain a character which is used to give a colour to each point when being plotted. Obviously this should not be used to classify the points.

'''
    Parametric Equation for a circle:
    x = b * t * cos(t + a)
    y = b * t * sin(t + a)
'''

a_1 = 0 # offset of spiral 1
a_2 = np.pi # offset of spiral 2
b_1 = 1 # tightness parameter of spiral 1
b_2 = 1 # tightness parameter of spiral 2

rot = 2 # rotations
t = 0 # parametric parameter within range [0, 2 * pi]
dt = rot * 2 * np.pi / N # increment of t such that dt = 2 * pi corresponds to one 'revolution'

for i in range(0, N):
    data_x[i] = b_1 * t * np.cos(t + a_1) + random.gauss(0, 0.3) # random gaussian noise added, mean 0, standard deviation of 2
    data_y[i] = b_1 * t * np.sin(t + a_1) + random.gauss(0, 0.3)
    t += dt
    labels.append('r')

t = 0
for i in range(N, data_points):
    data_x[i] = b_2 * t * np.cos(t + a_2) + random.gauss(0, 0.3)
    data_y[i] = b_2 * t * np.sin(t + a_2) + random.gauss(0, 0.3)
    t += dt
    labels.append('b')

plt.scatter(data_x, data_y, c = labels)
plt.show()