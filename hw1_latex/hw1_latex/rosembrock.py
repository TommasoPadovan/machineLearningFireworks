import numpy as np
import matplotlib.pyplot as plt
import math
import random

ITERATIONS = 10000
LEARNING_RATE = 1e-6

histX = []
x = np.array([random.uniform(0.0,3.0) for i in range(20)])

    
#Gradient of Rosenbrock function
def rosenbrockGradient(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    gradient = np.zeros_like(x)
    gradient[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    gradient[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    gradient[-1] = 200*(x[-1]-x[-2]**2)
    return gradient




for i in range(1, ITERATIONS):
    lastX = x
    x = x - LEARNING_RATE * rosenbrockGradient(x)
    histX.append(x)
    


plt.plot(histX[:])
plt.xlabel("steps")
plt.show()
