''' Calculation of Arithmatic-Geometric mean of two numbers
Plot of AGM with given Range '''

import math
import matplotlib.pyplot as plt

x = input("first no")
p = int(x)
y = input("second no.")
q = int(y)
n = input("range") # No of iterations for the sequence
r = int(n)
i = 0
a = []             # list of interdependent sequence
g = []
a.append(p)        # append the firdt no taken as input
g.append(q)

for i in range(r):
    h = 0.5 * (a[i] + g[i])         #    Calculate Arithmatic mean
    w = math.sqrt(a[i] * g[i])      # Calculate Geometric mean
    a.append(h)
    g.append(w)
print('\n{}'.format(a))
print('\n{}'.format(g))
# AGM plot
plt.xlabel('a number')
plt.ylabel('g number')
plt.title('AGM PLOT')
plt.plot(a, g)
plt.show()
