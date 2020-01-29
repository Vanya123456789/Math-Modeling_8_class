import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

t = np.arange(0.01,12*np.pi,0.01)
R=1

x = R*(2**-0.1*t*np.cos(t))
y = R*(2**-0.1*t*np.sin(t))
z = R*(t)
ax.plot(x,y,z,label ='balala')
ax.legend()

ax.set_xlabel('X')
ax.set_xlabel('Y')
ax.set_xlabel('Z')

ax.set.title('3D Test')

plt.show()

