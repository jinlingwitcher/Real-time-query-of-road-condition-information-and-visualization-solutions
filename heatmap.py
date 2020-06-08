# -*- coding: utf-8 -*- 
import matplotlib.pylab as plt
import numpy as np
import matplotlib

a=np.loadtxt(r'./1.csv',delimiter=',')

plt.matshow(a,cmap=plt.cm.Greys)
plt.axis('off') 
plt.show()
matplotlib.image.imsave("00.jpg",a)



