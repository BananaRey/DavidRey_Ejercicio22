import numpy as np
import matplotlib.pyplot as plt

archivo=np.loadtxt('dif.txt')

x=archivo[:,0]
u=archivo[:,1]
u_0=archivo[:,2]

plt.plot(x,u)
plt.plot(x,u_0)
#plt.ylim(0.0,1.5)
plt.title('Difusion',fontsize=25)
plt.xlabel('x',fontsize=25)
plt.ylabel('u(x,t)',fontsize=25)
plt.show()
plt.savefig('Difusion.png')
plt.close()
