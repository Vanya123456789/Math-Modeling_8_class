import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
R = 3
t = np.arange(-2*np.pi,2*np.pi,0.1)
x=R*(np.cos(t)**3)
y=R*(np.sin(t)**3)

plt.plot(x,y, linestyle = "--",linewidth = 5)
plt.show


