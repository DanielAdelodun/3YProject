import matplotlib.pyplot as plt
import numpy as np 

xmax = 1.5
xmin = 0
totalwidth = xmax - xmin
colour1 = 'red'
colour2 = 'purple'
colour3 = 'blue'
f = np.sin

x = np.linspace(xmin, xmax, num=21, endpoint=True)
y = f(x)

# sin graph
xs = np.linspace(xmin, xmax, 100)
ys = f(xs)

# Set up axes
fig, axes = plt.subplots(nrows=3, dpi=300, figsize=(2.5, 4))
fig.subplots_adjust(hspace = 0.075)
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
    ax.set_xlim(xmin, xmax)

x4 = x[::4]
x2 = x[::2]
x1 = x[::1]
ax1.bar(x4, f(x4), 
    align='edge', width=-(totalwidth/5), 
    fc=colour1, ec=colour1, alpha=0.3)
ax2.bar(x2, f(x2),
    align='edge', width=-(totalwidth/10),
    fc=colour2, ec=colour2, alpha=0.3)
ax3.bar(x1, f(x1), 
    align='edge', width=-(totalwidth/20),
    fc=colour3, ec=colour3, alpha=0.3)

fig.savefig('Area2.png')
#plt.show()
