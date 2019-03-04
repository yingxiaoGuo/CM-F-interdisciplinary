import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei'] #这两句用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False

#调参调到收敛点在左上角

x0=np.array([0,0,1/0.002,375])
y0=np.array([0,1/0.003,0,250])
#r1 r1*q/N1 delta1
p=[0.1, 0.002, 0.0001, 0.3, 0.003, 0.0002]
a,b,c,d,e,f=p
y, x = np.mgrid[-100:501:5,-100:601:5]
s = a*(1-b*x)*x-c*y*x
t = d*(1-e*y)*y-f*x*y
r = np.sqrt(s**2+t**2)
plt.figure(figsize=(7*1.2,6))
plt.plot([-100,600],[1/0.003,1/0.003], 'b--',alpha=0.5)
plt.plot([-100,600],[250,250], 'b--',alpha=0.5)
plt.plot([500,500],[-100,500], 'b--',alpha=0.5)
plt.plot([375,375],[-100,500], 'b--',alpha=0.5)
plt.plot([0,0],[-100,900], 'b--',alpha=0.5)
plt.plot([-100,600],[0,0], 'b--',alpha=0.5)
plt.scatter(x0,y0, s=75,color ='green',label='Equilibrium point')
plt.streamplot(x, y, s, t, color=r, density=1.5,linewidth=1, cmap=plt.cm.get_cmap('RdYlBu')) #get_cmap('RdYlBu')
plt.colorbar()
plt.xlim(300,601)
plt.ylim(-100,501)
plt.xlabel(u'$x$')
plt.ylabel(u'$y$')
plt.title(u'The phase plane of Predicted Financial Dynamical System')
plt.legend()
plt.show()
