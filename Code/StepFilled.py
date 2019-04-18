import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cm as cm
import numpy as np
import numpy.random as rand
# Added Filling
rand.seed(19)

fig, ax = plt.subplots(nrows=1, 
                       ncols=1,
                       subplot_kw={'xlim':(0,10), 'ylim':(-2,4)},
                       figsize=(4, 4),
                       dpi=300)

points = np.array([0, 2, 3, 6, 8, 10])
noPoints = len(points)
heights = np.random.randint(-1, 4, size=noPoints)

# Plot lines between adjecent points in 'points' at varying heights
for x in range(len(points) - 1):
    ax.hlines(heights[x], 
              points[x], 
              points[x+1], 
              linewidth=1.2, 
              linestyle='-', 
              color='k')
# Draw rectangle patches at those but coloured over integer steps
for y in range(10):
    for x in range(len(points)):
        if y >= points[x]:
            continue
        rect = patches.Rectangle((y, 0),
                                 1,
                                 heights[x-1],
                                 color=cm.spring(y/10),
                                 alpha=0.3)
        ax.add_patch(rect)
        break

# Dotted horizontal lines at the jumps
for i, x in enumerate(points[1:-1]):
    ax.vlines(x, heights[i], heights[i+1], linewidth=1,
              linestyle=':', color='grey')

# Also add a random point for the value of the funtion at x
atx = rand.randint(5, size=(noPoints-2))
ax.plot(points[1:-1], atx, 'ko', fillstyle='full')
ax.plot(points[1:-1], heights[1:-1], 'bo', fillstyle='none') 
ax.plot(points[1:-1], heights[:-2], 'bo', fillstyle='none') 

#plt.show()
plt.savefig('StepFilled.png')
