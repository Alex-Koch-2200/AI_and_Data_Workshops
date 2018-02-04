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

# The centres of each cloud. Make the difference between the two larger to make the classifcation easier
centre_1 = [40, 60]
centre_2 = [60, 40]

std_1 = 5 # standard deviation of cloud 1 (red)
std_2 = 5 # standard deviation of cloud 2 (blue)

for i in range(0, N):
    data_x[i] = random.gauss(centre_1[0], std_1) # mean is specified by the centre and the standard deviation is std_1
    data_y[i] = random.gauss(centre_1[1], std_1)
    labels.append('r')

for i in range(N, data_points):
    data_x[i] = random.gauss(centre_2[0], std_2)
    data_y[i] = random.gauss(centre_2[1], std_2)
    labels.append('b')

plt.scatter(data_x, data_y, c = labels)
plt.show()



