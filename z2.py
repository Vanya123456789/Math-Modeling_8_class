import numpy as np
def massiv(a):
    b = 1
    for i in range(0, len(a), 1):
        b = b*a[i]
    print(b)
    
a = np.arange(1,20,2)
massiv(a)