# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:52:16 2020

@author: color
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

#datos 
t=np.linspace(0,10,51)
x=np.linspace(-np.pi,np.pi,11)
y=np.linspace(-np.pi,np.pi,11)

xmesh,ymesh=np.meshgrid(x,y)

def f(x,y,t):
    return np.sin(y+t)*np.cos(x)

#grafitca
fig=plt.figure()
ax=fig.gca(projection='3d')

#actualizar
def actualizar(i):
    ax.clear()
    zmesh=f(xmesh,ymesh,t[i])
    ax.plot_surface(xmesh,ymesh,zmesh)
    plt.title(str(t[i]))

#animacion
ani=animation.FuncAnimation(fig,
                            actualizar,
                            range(len(t)),
                            interval=10,
                            repeat=True)

plt.show()