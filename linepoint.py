import numpy as np
import matplotlib.pyplot as plt
import seaborn

k=2
rng=np.random.RandomState(52)
x=rng.rand(10,2)
dist=np.sum((x[np.newaxis,:,:]-x[:,np.newaxis,:])**2,axis=-1)
nearest=np.argpartition(dist,k+1,axis=1)
plt.scatter(x[:,0],x[:,1],s=200)
for i in range(x.shape[0]):
    for j in nearest[i,:k+1]:
        plt.plot(*zip(x[i],x[j]),color='black')
plt.show()