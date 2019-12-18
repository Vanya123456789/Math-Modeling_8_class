import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,100,0.1)
def bakteria(n,t):
    dndt = k*n
    return dndt
k = 0.0
n_0 = 1
r = odeint(bakteria, n_0, t)
plt.plot(t, r)
plt.show()
