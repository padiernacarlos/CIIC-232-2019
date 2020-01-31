import numpy as np

def sphere(x):
    sum = 0
    for c in x:
        sum += c**2
    return sum

def rastrigin(x):
    sum = 0
    n = len(x)
    for c in x:
        sum += c**2 - 10*np.cos(2*np.pi*c)
    return 10*n + sum

def rosenbrock(x):
    sum = 0
    n = len(x)
    for i in range(n-1):
        sum += 100*(x[i+1] - x[i]**2)**2 + (1-x[i])**2
    return sum

def auckley(x):
    y = x[0]
    z = x[1]
    return -20*np.exp(-0.2*np.sqrt(0.5*(y**2+z**2)))-\
            np.exp(0.5*(np.cos(2*np.pi*y)+np.cos(2*np.pi*z)))+\
            np.exp(1)+20
def beale(x):
    y = x[0]
    z = x[1]
    return (1.5-y+y*z)**2 + (2.25-y+y*z**2)**2 +\
            (2.625-y+y*z**3)**2

def gold(x):
    y = x[0]
    z = x[1]

    return (1+((y+z+1)**2)*(19-14*y+3*y**2-14*z+6*y*z+3*z**2))*\
    (30+((2*y-3*z)**2)*(18-32*y+12*y**2+48*z-36*y*z+27*z**2))
