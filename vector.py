import numpy as np

mu, sigma = 0,1
r = np.random.normal(mu, sigma, 100)
def tozero(a):
        if a > 0:
            return a
        else:
            return 0
vfunc = np.vectorize(tozero)
print (vfunc(r))