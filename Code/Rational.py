import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

xmax = 5
fig, ax = plt.subplots(nrows=1, 
                       ncols=1,
                       subplot_kw={'xlim': (0, xmax),
                                   'ylim': (-0.25, 1.5)}, 
                       figsize=(5, 2.5), 
                       dpi=300)

# Add a solid line at 0.
ax.axhline(0, 0, 1)

# Mark negative powers of two with shrinking x markers
# Higher negative power --> Finer markings --> Smaller marker sizes
for n in range(5):
    num = xmax * 2**(n) 
    pnum = -1 if n == 0 else xmax * 2**(n-1)  

    points = np.linspace(0, xmax, num+1, endpoint=True)
    ppoints = np.linspace(0, xmax, pnum+1, endpoint=True)
    
    xs = [x for x in points if x not in ppoints]
    ys = np.ones(len(xs))

    ax.scatter(xs, ys, 
               c=[cm.winter(0.5 + n/11)], 
               s=50/((n+1)*2**(n)), 
               marker='x')

#plt.show()
plt.savefig('Rational.png')
