import matplotlib.pyplot as plt
import numpy as np 
# from scipy.interpolate import interp1d

colour1 = 'red'
colour2 = 'blue'

x = np.linspace(0, 1.5, num=11, endpoint=True)
y = np.sin(x)

# sin graph
xs = np.linspace(0, 1.5, 100)
ys = np.sin(xs)

# Set up axis
fig, axes = plt.subplots(nrows=3, dpi=72, figsize=(5, 8))
ax1, ax3, ax2 = axes
i = 0
for ax in axes:
    ax.plot(xs, ys, 'r-') 
    #if i != 0:
       # ax.plot(x, y, 'ro') 
    #if i != 2:
       # ax.plot(x[::2], y[::2], 'go')
    ax.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=False, labelright=False, labeltop=False)
    i += 1
    ax.set_xlim(0, 1.5)
   
ax1.bar(x[::2], np.sin(x[::2]), align='edge', width=-(1.5/5), fc=colour2, ec=colour2, alpha=0.3)
ax2.bar(x[:], np.sin(x[:]), align='edge', width=-(1.5/10), fc=colour1, ec=colour1, alpha=0.2)

ax3.bar(x[::2], np.sin(x[::2]), align='edge', width=-(1.5/5), fc=colour2, ec=colour2, alpha=0.3)
ax3.bar(x[:], np.sin(x[:]), align='edge', width=-(1.5/10), fc=colour1, ec=colour1, alpha=0.2)

fig.tight_layout()
plt.show()
