import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.cm as cm
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable


# Each entry in step is the result from one cycle of the approximation.
# So step[2] contains the data for when the appoximating simple function has a height of 2.
# The data being the a dictionary with key/value pairs where 
# key = k * 2^(-STEP) for k up to STEP * 2^(STEP) (i.e. the lower bound of the set we are finding the inverse of).
# value = The set of xs such that f(x) is in [ key , key + 2^(-STEP) )
MAX_STEP = 4
step = []
GRAN = 500
X_MAX = 10
POINT_SIZE = X_MAX/GRAN
def ss(x):
    return 2**(-x)
DH_DEFAULT = ss(2)
def colour(x=1.0):
    r = list(cm.winter(x/4))
    r[3] = 0.5
    return tuple(r)


# Set up the axes.
fig, axes = plt.subplots(nrows=2, ncols=2, dpi=72, figsize=(10, 10))
for ax_rows in axes:
    for ax in ax_rows:
        ax.set_xlim(0,10)
        ax.set_ylim(0, 4)
        ax.tick_params(
           axis='both',       # changes apply to both axis
           which='both',      # both major and minor ticks are affected
           bottom=False,      # ticks along the bottom edge are off
           top=False,         # ticks along the top edge are off
           left=False,
           labelleft=False, 
           labelbottom=False) # labels along the bottom edge are off
(ax1, ax2), (ax3, ax4) = axes

fig2, axes2 = plt.subplots(nrows=2, ncols=2, dpi=72, figsize=(10, 10))
for ax_rows in axes2:
    for ax in ax_rows:
        ax.set_xlim(0,10)
        ax.set_ylim(0, 4)
        ax.tick_params(
            axis='both',       # changes apply to both axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            left=False,
            labelleft=False,
            labelbottom=False) # labels along the bottom edge are off
(ax21, ax22), (ax23, ax24) = axes2


# Set up the graph.

# Our graph in this case is drawn by interpolation.
xs = np.linspace(0, 10, num=5, endpoint=True)
ys = [0, 1.75, 0.9, 2.5, 2.5]

# Can change the definition of f to any function which takes a float and returns another float.
f = interp1d(xs, ys, kind='cubic') # Here, though, we are just interpolating between the given points.
xnew = np.linspace(0, 10, num=GRAN+1, endpoint=True)
ynew = f(xnew)

# step.append({0:''})

for STEP in range(0, MAX_STEP+1):
    # Add a new dictionary for this cycles data
    step.append({})
    # Determine the heights of the level sets
    dh = ss(STEP)
    # Look at each level seperately, and identfiy it by it's 'y_base' - the y lower bound
    for y_base in np.arange(0, STEP, dh):
        # Find all the x points which where mapped to some y in the level set we are currently focused on.
        # Add those values to our step data dictionary under the current step.
        step[STEP][y_base] = list(filter(lambda x: f(x) >= y_base and f(x) < (y_base + dh), xnew))
       

c_step = 1
# Plot a grid of graphs, which each showing a different step of the approximation.
for ax_rows in axes:
    for ax in ax_rows:
        DH = ss(c_step)
        # Plot the graph on each axis
        ax.plot(xnew, ynew, color='0.1', lw=0.5, linestyle='-')
        for y_base in np.arange(0, 4, DH):
            # For each step/axes, only color the graph up to height of the appoximating simple function.
            if y_base >= 0 and y_base < c_step:
                if y_base >= 1 and y_base < 1.5:
                    ax.axhline(y_base, lw=0.5, color='k', alpha=0.7, linestyle='-.')
                    ax.axhspan(y_base, y_base+DH, facecolor=colour(y_base), edgecolor='none')
                ax.axhspan(y_base, y_base+DH, facecolor=colour(y_base), edgecolor='none')
        ax_divider = make_axes_locatable(ax)
        cax = ax_divider.append_axes("bottom", size="5%", pad="2%")
        cax.set_xlim(0,10)
        cax.set_ylim(3.7,3.8)
        cax.tick_params(
            axis='both',       # changes apply to both axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            left=False,
            labelleft=False,
            labelbottom=False) # labels along the bottom edge are off
        cax.axis('off')
        for y_base in np.arange(0, c_step, ss(c_step)):
                xmatch = step[c_step][y_base]  
                cax.scatter(xmatch, [3.75]*len(xmatch), s=15, c=[colour(y_base)], marker='s')
                print(xmatch)
        c_step += 1

#  For the graph representing step[2], for instance;
#  - The heights of the bars should be k * ss(2) up to 2 - ss(2)
#  - The width of the bar at height k * ss(2) = y_base should be "the number of x's mapped between 
#       y_base and y_base + ss(2) * 'the measure' of a single x"; so it'll be len(step[2][y_base]) * POINT_SIZE.
c_step = 1
for ax_rows in axes2:
    for ax in ax_rows:
        # Starting from a bar of height 0 up to a bar of height ' c_step - ss(c_step) ', create vbars with heights k * ss(c_step) and widths ...
        m = [0]
        DH = ss(c_step)
        for y_base in np.arange(0, c_step, DH):
            # Set the right x boundary of the vbar as "the left boundary + 'measure' of the set of xs mapped to range we are intrested in".
            m.append(m[-1] + len(step[c_step][y_base]) * POINT_SIZE)
            xmin = m[-2]
            xmax = m[-1]
            # Draw vbar.
            y_base = y_base + 0.01 if y_base == 0 else y_base
            if y_base >= 1 and y_base < 1.5:
                ax.axvspan(xmin, xmax, ymax=y_base/4, facecolor=colour(y_base), edgecolor='k')
            ax.axvspan(xmin, xmax, ymax=y_base/4, facecolor=colour(y_base)) 
        c_step += 1



plt.show()
