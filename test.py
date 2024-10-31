import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return 4*x**2+3*x+1

#tracé de la courbe u=f(x)

x = np.arange(-3.0,3.0,0.01)
y=function(x)
plt.plot(x,y,'r-')

def functionprime(x):
    return 8*x+3

#### gradient algorythm

etq = 0.1
eps= 0.0001
x0=2

plt.scatter (x0,functionprime(x0))
print (x0, function(x))

cond = abs(functionprime(x0))

while cond > eps:
    x0=x0 - etq*functionprime
    y0= function(x0)
    plt.scatter(x0,y0)
    cond= abs(functionprime(x0))
    