from scipy import optimize
import numpy as np
def f(x):
    return (x[0]-2.3)**2+(x[1]-0.1)**2 + 3
#print(f([2.3,0.1]))
# m=optimize.minimize(f,[0,0])
# print(m)
# m.x

# from scipy import linalg
# a=np.array([[3,2,0],[1,-1,0],[0,5,1]])
# b=np.array([2,4,-1])
# x=linalg.solve(a,b)
# print(a)
# print(x)
# c=np.dot(a,x)
# print(c)

from matplotlib import pylab as plt
# plt.plot([1,2,3,4],[1,4,6,9])
# plt.show()
# x=np.arange(-10,10,0.1)
# y=x**3
# plt.plot(x,y)
# plt.show()

x=np.arange(-2*np.pi,2*np.pi,1)
y=np.sin(x)

from scipy import interpolate
# x=np.arange(0,10,2)
# y=np.exp(-x/2)

f1=interpolate.interp1d(x,y,kind='nearest')
x1=np.arange(-2*np.pi,2*np.pi-1,0.1)
y1=f1(x1)
#plt.plot(x1,y1)
plt.plot(x,y,'x',x1,y1,'-')
plt.show()
