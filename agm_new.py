''' Calculation of Arithmatic-Geometric mean of two numbers
Plot of AGM with given Range '''

import math
import matplotlib.pyplot as plt
import numpy as np

p = 200
q = 5
r = 4
i = 0
a = []             # list of interdependent sequence
g = []
a.append(p)        # append the first no taken as input
g.append(q)
x_axis=np.linspace(0,r,r+1)
for i in range(r):
    h = 0.5 * (a[i] + g[i])         #    Calculate Arithmatic mean
    w = math.sqrt(a[i] * g[i])      # Calculate Geometric mean
    a.append(h)
    g.append(w)

print('\n{}'.format(a))
print('\n{}'.format(g))
# AGM plot

plt.plot(x_axis, a,label = "arithmetic mean")# plotting arithmetic mean values vs iteration
plt.plot(x_axis,g,label='geometric mean')#plotting geometric mean values vs iteration

plt.xlabel('Iteration')
plt.ylabel('Number')
plt.title('AGM PLOT')
plt.legend()
plt.show()
