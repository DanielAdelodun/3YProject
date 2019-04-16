import matplotlib.pyplot as plt
import numpy as np 
# from scipy.interpolate import interp1d

colour1 = 'red'
colour2 = 'purple'
colour3 = 'blue'

x = np.linspace(0, 1.5, num=21, endpoint=True)
y = np.sin(x)

# sin graph
xs = np.linspace(0, 1.5, 100)
ys = np.sin(xs)

# Set up axis
fig, axes = plt.subplots(nrows=3, dpi=300, figsize=(3, 4))
ax1, ax2, ax3 = axes
for ax in axes:
    ax.plot(xs, ys, 'g-') 
    ax.tick_params(top=False, 
                   bottom=False, 
                   left=False, 
                   right=False, 
                   labelleft=False, 
                   labelbottom=False, 
                   labelright=False,
                   labeltop=False)
    ax.set_xlim(0, 1.5)
   
ax1.bar(x[:-1:4], np.sin(x[:-1:4]), align='edge', width=(1.5/5), fc=colour3, ec=colour3, alpha=0.3)
ax2.bar(x[:-1:2], np.sin(x[:-1:2]), align='edge', width=(1.5/10), fc=colour2, ec=colour2, alpha=0.3)
ax3.bar(x[:-1], np.sin(x[:-1]), align='edge', width=(1.5/20), fc=colour1, ec=colour1, alpha=0.3)

fig.tight_layout()
fig.savefig('Area1.png')
plt.show()
