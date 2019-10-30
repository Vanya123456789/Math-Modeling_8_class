from constant import g,M,R,k,h,e
from math import pi,sqrt
print(pi)
print(sqrt)
h = 100
v = sqrt(g*h*pi/(2*M*R))
print(v)
T = 200
epsilon = 300
N = (2/sqrt(pi))*(h/((k*T)**1.5))*e**(-epsilon/k*T)*epsilon**(T/2)
print(N)