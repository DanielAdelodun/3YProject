# f(x) -----> number.

import matplotlib.pyplot as plt
import numpy as np 

n = 6

xmax = 6
xmin = 0
totalwidth = xmax - xmin

# 160 points equally spaced points (plus zero) in the domain
num = (5 * 2**(n-1)) + 1
x = np.linspace(xmin, xmax, num=num, endpoint=True)

# Make a list of 'n' colours
colour1 = '#95d0fc' #light blue
colour2 = '#75bbfd' #sky blue
colour3 = '#00ffff' #cyan
colour4 = '#13eac9' #aqua
colour5 = '#929591' #grey
colour6 = '#06c2ac' #turquoise
colour = [colour1, colour2, colour3, colour4, colour6, colour5]

f = np.sin

y = f(x)

# To draw graph
xs = np.linspace(xmin, xmax, 100)
ys = f(xs)

fig, axesr = plt.subplots(nrows=int(n/2), ncols=2, dpi=300, figsize=(5, n*3/4))
fig.subplots_adjust(hspace = 0.075)
axes = [ax for axes in axesr for ax in axes]

fig.subplots_adjust(wspace=0.05, hspace=0.075)

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

reps = [x[:-1:2**n] for n in range(n)]
bars = [(x, []) for x in reps]
for interval_steps, bar in zip(reps, bars):
    for i in range(len(interval_steps)):
        xright = xmax if i == len(interval_steps) - 1 else interval_steps[i+1]
        xleft = interval_steps[i]
        interval = np.linspace(xleft, xright, 1000)
        interval_mapped = [f(x) for x in interval]
        interval_min = min(interval_mapped) ## Can change 'min' to 'max'
        bar[1].append(interval_min)         ## to bound from above

i = n
for ax in reversed(axes):
    i -= 1
    div = 5 * 2**i
    ax.bar(*bars[n-i-1], 
        align='edge', width=(totalwidth/div), 
        fc=colour[i], ec=colour[i], alpha=0.95)

fig.savefig('RiemannExample.png')
