import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig= plt.figure()
def parabola_f(a,b,c,N):
    x=np.linspace(-5,5,N)
    y=np.zeros(N)
    for i in range(N):
        y[i]=a*x[i]**2+b*x[i]+c
    return x,y
def circle_f(x_centre,y_centre, R, N):
    x=np.zeros(N)
    y=np.zeros(N)
    for i in range(N):
        alpha=np.linspace(0,2*np.pi,100)
        x[i]=x_centre+R*np.cos(alpha[i])
        y[i]=y_centre+R*np.sin(alpha[i])
    return x,y
anim_list=[]
N=100
x=[]
y=[]
for i in range(N):
    x,y = parabola_f(a=3,b=2,c=1,N=100)
    x_circle, y_circle = circle_f(x_centre=x[i],y_centre=y[i], R=8, N=100)
    parabola,= plt.plot(x[:i+1], y[:i+1],'k-', lw=2)
    circle,= plt.plot(x_circle, y_circle, 'b-', lw=2)
    tochka,= plt.plot(x[i],y[i],'ro')
    anim_list.append([parabola, circle, tochka])
ani=ArtistAnimation(fig,anim_list, interval=50)
plt.axis('equal')
ani.save('parabola.gif')