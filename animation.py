import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
R = 3
t = np.arange(-2*np.pi,2*np.pi,0.1)
fig,ax = plt.subplots()
anim_object, =plt.plot([],[],'o')
xdata,ydata = [],[]
 
ax.set_xlim(-2, 2)
ax.set_ylim(-2,2)


def update(t):
    ydata.append(np.sin(t))
    xdata.append(np.cos(t))
    anim_object.set_data(xdata,ydata)
    return anim_object,

ani = FuncAnimation(fig,
                    update,
                    frames = np.arange(-2*np.pi, 2*np.pi, 0.1),
                    interval=50)

ani.save("animacha.gif")