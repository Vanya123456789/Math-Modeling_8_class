import numpy as np
from constant import g
x0 = 1
y0 = 2
v0x = 3
v0y = 4
t = np.arange(0,5,0.01)
print(t)
N = len(t)
coord_and_vel=np.ndarray(shape = (N,3))
for i in range(0,N,1):
    x = x0 + v0x*t[i]
    y = y0 + v0y*t[i] - (g*t[i]**2)/2
    coord_and_vel[i,0]=t[i]
    coord_and_vel[i,1]=x
    coord_and_vel[i,2]=y
print(coord_and_vel)
