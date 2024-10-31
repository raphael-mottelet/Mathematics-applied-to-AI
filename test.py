import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return 4*x**2+3*x+1

#tracé de la courbe u=f(x)

x = np.arange(-3.0,3.0,0.01)
y=function(x)
plt.plot(x,y,'r-')
