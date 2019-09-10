import numpy as np
import matplotlib.pyplot as plt
import seaborn 

seaborn.set()
rng=np.random.RandomState(42)
x=rng.rand(10,2)
dist_sq=np.sum((x[:,np.newaxis,:]-x[np.newaxis,:,:])**2,axis=-1)
plt.scatter(x[:,0],x[:,1],s=100)
plt.show()
