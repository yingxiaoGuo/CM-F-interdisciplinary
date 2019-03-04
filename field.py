import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei'] #这两句用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False

p=[0.123, 0.0881, 0.0881, 0.3, 0.003, 0.0002]
x0=np.array([0,0,1/0.002,375])
y0=np.array([0,1/0.003,0,250])
a,b,c,d,e,f=p
x,y = np.mgrid[-100:601:25,-100:501:25]
#x,y = np.mgrid[300:401:5,200:300:5]
s = a*(1-b*x)*x-c*y*x
t = d*(1-e*y)*y-f*x*y
r = np.sqrt(s**2+t**2)
plt.figure(figsize=(7*1.2,6))
plt.plot([-100,600],[1/0.003,1/0.003], 'r--',alpha=0.5)
plt.plot([-100,600],[250,250], 'r--',alpha=0.5)
plt.plot([500,500],[-100,500], 'r--',alpha=0.5)
plt.plot([375,375],[-100,500], 'r--',alpha=0.5)
plt.scatter(x0,y0, s=75,color ='green',label='Equilibrium point')
plt.quiver(x,y,s/r,t/r,r)
plt.colorbar()
plt.xlim(-100,601)
plt.ylim(-100,501)
plt.xlabel(u'$x_1$')
plt.ylabel(u'$x_2$')
plt.title(u'The vector field of Predicted Financial Dynamical System')
plt.legend()
plt.show()