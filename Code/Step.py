import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rand

rand.seed(1)

fig, ax = plt.subplots(nrows=1, 
                       ncols=1,
                       subplot_kw={'xlim':(0,10), 'ylim':(-1,5)},
                       figsize=(5, 5),
                       dpi=300)

points = np.array([0, 2, 3, 6, 8, 10])
noPoints = len(points)
heights = np.random.randint(5, size=noPoints)

# Plot lines between adjecent points in 'points' at varying heights
for x in range(len(points) - 1):
    ax.hlines(heights[x], points[x], points[x+1], linewidth=1.2, linestyle='-', color='k')

# Dotted horizontal lines at the jumps
for i, x in enumerate(points[1:-1]):
    ax.vlines(x, heights[i], heights[i+1], linewidth=1,
              linestyle=':', color='grey')

# Also add a random point for the value of the funtion at x
atx = rand.randint(5, size=(noPoints-2))
ax.plot(points[1:-1], atx, 'ko', fillstyle='full')
ax.plot(points[1:-1], heights[1:-1], 'bo', fillstyle='none') 
ax.plot(points[1:-1], heights[:-2], 'bo', fillstyle='none') 

plt.tight_layout()
plt.show()
