import math
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import submission as submission
# %matplotlib inline  


def f(x):
    return x * math.log(x) - 16.0

def fprime(x):
    return 1.0 + math.log(x)

# xvals = np.arange(0.01, 10, 0.01)        
# yvals = np.array([f(x) for x in xvals])
# plt.plot(xvals, yvals) 
# plt.plot(xvals, 0*xvals)
# plt.show()
x = submission.find_root(f, fprime)
print(x)
print(f(x))

