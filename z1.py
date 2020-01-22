import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 10, 0.01)
def dif(z,t):
    y, w=z
    dydt=w
    dwdt=-np.sin(y)*w-3*y*t-5
    return dydt, dwdt
y0=3
w0 = 0.05
z0 =y0,w0
solve=odeint(dif,z0,t)
plt.plot(t, solve[:,0])
plt.show()