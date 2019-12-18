import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,10,0.1)
m = 15
def tochka(v,t):
    dvdt = (F-k*v**2)/m
    return dvdt

k = 0.08
v_0 = 0
F = 150
zakon_nutona = odeint(tochka, v_0, t)
plt.plot(t, zakon_nutona , label = 'бег в воде')
plt.title('бег в воде')
plt.xlabel('Время')
plt.ylabel('Скорость')
plt.show()
    

