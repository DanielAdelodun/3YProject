import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

fig, ax = plt.subplots(nrows=1, ncols=1, subplot_kw={'xlim': (0, 5), 'ylim': (-0.25, 1.5)}, figsize=(3, 3), dpi=300)
fig.tight_layout()

# Add a solid line at y=0.
ax.plot([0, 5], [0, 0])

# Mark negative powers of two with shrinking x markers
pl = []
ply = []
for n in range(5):
    num = 5 * 2**n + 1
    pnum = 5 * 2**(n-1) + 1

    points = np.linspace(0, 5, num, endpoint=True)
    ppoints = np.linspace(0, 5, pnum, endpoint=True)
    xs = [x for x in points if x not in ppoints]
    pl.append(xs)

    ys = np.ones(len(xs))
    ply.append(ys)
    ax.scatter(xs, ys, c=[cm.winter(0.5 + n/11)], s=50/((n+1)*2**(n)), marker='x')
plt.show()
