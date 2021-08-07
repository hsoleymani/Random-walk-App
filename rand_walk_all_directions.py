# Code for a bee walking on hexagone combs.
import streamlit as st
import numpy 
import random
from scipy.spatial import distance
import matplotlib as plt


# defining the number of steps
st.sidebar.header('Random Walk')

# Add a sidebar
n = st.sidebar.number_input('Insert a number of steps',min_value=1, step=10)+1
nn = st.sidebar.number_input('Insert a number of run',min_value=10, step=100)

x = numpy.zeros(n)
y = numpy.zeros(n)
dst = []
mean_dst = []

# looping over large numver of trials
for m in range(1,nn):


    # coordinates for hexagonal shape
    for i in range(1, n):
        val = random.randint(1, 6)
        if val == 1:
            x[i] = x[i - 1] + numpy.sqrt(3)/2
            y[i] = y[i - 1] + 0.5
        elif val == 2:
            x[i] = x[i - 1] + 0
            y[i] = y[i - 1] + 1
        elif val == 3:
            x[i] = x[i - 1] - numpy.sqrt(3)/2
            y[i] = y[i - 1] + 0.5
        elif val == 4:
            x[i] = x[i - 1] - numpy.sqrt(3)/2
            y[i] = y[i - 1] - 0.5
        elif val == 5:
            x[i] = x[i - 1] + 0
            y[i] = y[i - 1] - 1
        elif val == 6:
            x[i] = x[i - 1] + numpy.sqrt(3)/2
            y[i] = y[i - 1] - 0.5
    # calculate the distance in every run and store the distances
    dst.append(distance.euclidean([0,0], [x[n-1],y[n-1]]))
    mean_dst.append(numpy.meant(dst))

# plotting section:

fig = plt.pyplot.figure()

plt.pyplot. subplots_adjust(hspace = .3)

ax1 = fig.add_subplot(3,1,1)
ax1.plot(x, y, alpha=0.8)
ax1.set_xlabel('Distance')
ax1.set_ylabel('Distance')
ax1.set_title("Random Walk ($n = " + str(n) + "$ steps)")
ax1.scatter(x, y)
ax1.scatter(x[0], y[0], c='r', label="Start")
ax1.scatter(x[n-1],y[n-1], c='k', label="End")
ax1.legend(loc='upper left')


ax2 = fig.add_subplot(3,1,2)
ax2.hist(dst, density=True, histtype='bar', ec='black')
ax2.set_xlabel('Distance')
ax2.set_ylabel('Prob Density')

ax3 = fig.add_subplot(3,1,3)
ax3.plot(mean_dst)
ax3.set_xlabel('number of runs')
ax3.set_ylabel('Mean dist')

st.write(fig)
