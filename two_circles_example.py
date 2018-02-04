'''
Alex Koch
AI and Data Workshops 2018
MANSEDS (Manchester Students for the Exploration and Development of Space)
http://manseds.co.uk

Descripton: Data set of two circles, one inside the other with added random Gaussian noise.
Exercise: Classify the data points according to which circle they belong to and output in an 
          appropriate fashion.

An example solution(s) is provided in a separate file
'''

import random
import numpy as np
import matplotlib.pyplot as plt

data_points = 200
N = int(data_points / 2) # number of points per set

data_x = np.zeros([data_points])
data_y = np.zeros([data_points])
labels = [] # This will contain a character which is used to give a colour to each point when being plotted. Obviously this should not be used to classify the points.

'''
    Parametric Equation for a circle:
    x = a + r * cos(t)
    y = b + r * sin(t)
    centre (a,b) , t = [0, 2* pi], radius r
'''

centre_1 = [50, 50]
centre_2 = [50, 50]
r_1 = 20 # radius of circle 1
r_2 = 40 # radius of circle 2

t = 0 # parametric parameter within range [0, 2 * pi]
dt = 2 * np.pi / N # increment of t so that t ranges from 0 to 2 * pi over N steps

for i in range(0, N):
    data_x[i] = centre_1[0] + r_1 * np.cos(t) + random.gauss(0,2) # random gaussian noise added, mean 0, standard deviation of 2
    data_y[i] = centre_1[1] + r_1 * np.sin(t) + random.gauss(0,2)
    t += dt
    labels.append('r')

t = 0
for i in range(N,data_points):
    data_x[i] = centre_2[0] + r_2 * np.cos(t) + random.gauss(0,2)
    data_y[i] = centre_2[1] + r_2 * np.sin(t) + random.gauss(0,2)
    t += dt
    labels.append('b')

plt.scatter(data_x, data_y, c = labels)
plt.show()
