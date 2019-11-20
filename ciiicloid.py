import matplotlib.pyplot as plt
import numpy as np
R = 3
t = np.arange(-2*np.pi,2*np.pi,0.1)
x = R*(t-np.sin(t))
y = R*(1-np.cos(t))

plt.plot(x,y, linestyle = "--",linewidth = 5)
plt.show