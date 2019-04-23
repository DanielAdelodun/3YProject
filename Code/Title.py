import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import matplotlib.cm as cm
from scipy.interpolate import interp1d
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

# How many appoximations?
STEPS = 4

###

GRAN = 500
X_MIN = 0
X_MAX = 10
POINT_SIZE = (X_MAX-X_MIN)/GRAN

###

def colour(x=1.0):
    r = list(cm.winter(x/STEPS))
    r[3] = 0.4  # I think it looks better with a lower 'alpha'
    return tuple(r)

# We will be calculating 2^(-n) a lot to figure out the step size
# So this is a function to do that
def ss(x):
    return 2**(-x)

# Set up the graph and function.
# Our graph in this case is drawn by interpolation,
# but you can change the definition of f to any function
# which takes a float and returns another float.
xi = np.linspace(X_MIN, X_MAX, num=5, endpoint=True)
yi = [0, 1.75, 0.9, 2.5, 2.5]
f = interp1d(xi, yi, kind='cubic')
# The points we use to plot our graph
# and find the inverses of the levels; the level sets
xs = np.linspace(X_MIN, X_MAX, num=GRAN+1, endpoint=True)
ys = f(xs)

# Set up the axes.
# For the first half
fa1 = plt.subplots(nrows=int(STEPS**0.5), ncols=int(STEPS**0.5),
                   dpi=300, figsize=(5, 5))
fig1, axes1r = fa1
fa1 = list(fa1)
# For the second half
fa2 = plt.subplots(nrows=int(STEPS**0.5), ncols=int(STEPS**0.5),
                   dpi=300, figsize=(5, 5))
fig2, axes2r = fa2
fa2 = list(fa2)

for fig in [fig1, fig2]:
    fig.subplots_adjust(wspace=0.085, hspace=0.05)
fig2.subplots_adjust(hspace=0.085)
axes1 = [ax for axrows in axes1r for ax in axrows]
axes2 = [ax for axrows in axes2r for ax in axrows]
fa1[1] = axes1
fa2[1] = axes2
for fig, axes in [fa1, fa2]:
    for ax in axes:
        ax.set_xlim(X_MIN, X_MAX)
        ax.set_ylim(0, 4) # For this example specifically
        ax.tick_params(
           axis='both',
           which='both',
           bottom=False,
           top=False,
           left=False,
           labelleft=False,
           labelbottom=False)

###

# Calculate the level_sets.
# Code makes this easy, the difficulty is in how to organise the data
# The way I do it here is for every step in the the approximation, n,
# I have a dictionary with key vaule pairs 
#                           y_j : X_j = f^(-1)((y_j, y_j+step_size))
# And those dictionaries are kept in another dictionary called 
# all 'level_sets'. So all_level_sets[n][y_base] gives the level set
# for [y_base, y_base + step_size) for the step n
all_level_sets = {}
for j in range(1, 1+STEPS):
    step_size = ss(j)
    y_bases = np.arange(0, j, step_size)
    level_sets = {}
    for y_base in y_bases:
        X = [x for x in xs if \
             f(x) >= y_base and f(x) < y_base + step_size]
        level_sets[y_base] = X
    all_level_sets[j] = level_sets

# For the first figure, we want to visualise what's going on by colouring
# the different levels, and then underneath the graph the we show the level
# sets in matching colours. Unfortunately, since some many points overlap,
# this might not be obvious...
for step, ax in enumerate(axes1, 1):
    ax.plot(xs, ys, color='0.1', lw=0.5, linestyle='-')
    step_size = ss(step)
    y_bases = np.arange(X_MIN, step, step_size)
    for y_base in y_bases:
        ax.axhspan(y_base, y_base + step_size, # Colour the different levels 
            facecolor=colour(y_base), 
            edgecolor='none')
        if y_base >= 1 and y_base <= 1.5: # Highlight this section 
            ax.axhline(y_base, 
                       lw=0.5, 
                       color='k', 
                       alpha=0.7, 
                       linestyle='-.'
                      )
#            ax.axhspan(y_base, y_base + step_size,
#                       facecolor=colour(y_base), 
#                       edgecolor='none'
#                      )
            
    # Add a colour bar at the bottom, showing the different level
    # sets in different colours.
    # I wish I had a better way to do this...
    ax_divider = make_axes_locatable(ax)
    cax = ax_divider.append_axes("bottom", size="2%", pad="2%")
    cax.set_xlim(0,10)
    cax.set_ylim(0,0.1)
    cax.tick_params(
    axis='both',       
    which='both',      
    bottom=False,      
    top=False,         
    left=False,
    labelleft=False,
    labelbottom=False) 
    cax.axis('off')
    for y_base in np.arange(X_MIN, step, step_size):
        xmatch = all_level_sets[step][y_base]  
        cax.scatter(xmatch, [0.05]*len(xmatch), 
                    s=15, c=[colour(y_base)], marker='s')   

# For the second figure, we'd like to rearrange points in the domain, so
# that points in the same level set are next to each other.
# This can be done by just counting the number of points in a level set,
# then making a rectangle which has a width to this size.
for step, ax in enumerate(axes2, 1):
    step_size = ss(step)
    y_bases = np.arange(X_MIN, step, step_size)
    left_edge = 0
    for y_base in y_bases:
        no_of_xs = len(all_level_sets[step][y_base])
        measure = POINT_SIZE * no_of_xs
        # Draw boxes around the rectangles correspoding to the highlighted 
        # level sets.
        right_edge = measure
        rect = patches.Rectangle((left_edge, 0),
                                 measure,
                                 height=y_base,
                                 color=colour(y_base))
        if y_base >= 1 and y_base < 1.5:
            rect.set_edgecolor('k')
            rect.set_linewidth(0.7)
        ax.add_patch(rect)
        left_edge += measure
fig1.savefig('Title1.png')
fig2.savefig('Title2.png')
