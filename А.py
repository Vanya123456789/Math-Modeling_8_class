import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure()
a = 5
x = np.linspace(-5,5,100)
y = a*x**2
anim_list=[]
for i in range(len(x)):
    anim_object,=plt.plot(x[i],y[i],'o')
    anim_list.append([anim_object])
ani = ArtistAnimation(fig, anim_list, interval = 100)
ani.save('ani.gif')
