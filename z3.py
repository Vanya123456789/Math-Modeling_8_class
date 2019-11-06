import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(R = 1, a = 2,b=3,title='Circle and Okruzhnost'):
    x = np.arange(-2.0,2.0,0.1)
    y = np.arange(-2.0,2.0,0.1)
    X,Y = np.meshgrid(x,y)
    fxy = X**2+Y**2
    fxy1 = (X**2/a**2)+(Y**2/b**2) 
    plt.contour(X,Y,fxy,levels = [R])
    plt.contour(X,Y,fxy1,levels = [0.3])
    plt.show()

circle_plotter(0.5)

