import matplotlib.pyplot as plt
import numpy as np 

xmax = 2
xmin = 0
totalwidth = xmax - xmin
colour1 = 'red'
colour2 = 'purple'
colour3 = 'blue'
f = np.sin

# 20 points equally spaced points (plus zero) in the domain
x = np.linspace(xmin, xmax, num=21, endpoint=True)
y = f(x)

# To draw graph
xs = np.linspace(xmin, xmax, 100)
ys = f(xs)

# Set up axes
fig, axes = plt.subplots(nrows=3, dpi=300, figsize=(2.5, 3.5))
fig.subplots_adjust(hspace = 0.075)
ax1, ax2, ax3 = axes
for ax in axes:
    ax.plot(xs, ys, 'g-', linewidth=0.5) 
    ax.tick_params(top=False, 
                   bottom=False, 
                   left=False, 
                   right=False, 
                   labelleft=False, 
                   labelbottom=False, 
                   labelright=False,
                   labeltop=False)
    for axis in ['top','bottom','left','right']:
      ax.spines[axis].set_linewidth(0.4)

    ax.set_xlim(xmin, xmax)

# Skinny --> Wide
x1, x2, x4 = [x[:-1:2**n] for n in range(3)]
bar1, bar2, bar4 = [(x, []) for x in [x1, x2, x4]]
for interval_steps, bar in zip([x1, x2, x4], [bar1, bar2, bar4]):
    for i in range(len(interval_steps)):
        xright = xmax if i == len(interval_steps) - 1 else interval_steps[i+1]
        xleft = interval_steps[i]
        interval = np.linspace(xleft, xright, 1000)
        interval_mapped = [f(x) for x in interval]
        interval_max = max(interval_mapped)
        bar[1].append(interval_max)

ax1.bar(*bar4, 
    align='edge', width=(totalwidth/5), 
    fc=colour1, ec=colour1, alpha=0.3)
ax2.bar(*bar2,
    align='edge', width=(totalwidth/10),
    fc=colour2, ec=colour2, alpha=0.3)
ax3.bar(*bar1, 
    align='edge', width=(totalwidth/20),
    fc=colour3, ec=colour3, alpha=0.3)

fig.savefig('Area4.png')
#plt.show()
