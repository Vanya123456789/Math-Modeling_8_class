import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0,35,0.1)
def dif(z,t):
    s,v =z
    dsdt=v
    dvdt=-g*np.sin(s/l)-k/m*v
    return dsdt, dvdt
l=3
g=9.81
k=0.5
m=5
s0=5
v0=0
z0=s0,v0
solve=odeint(dif,z0,t)
plt.plot(t,solve[:,0])
plt.show()
