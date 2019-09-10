from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
num_friends = [49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
friend_counters=Counter(num_friends)
xs=range(100)
ys=[friend_counters[x] for x in xs]
plt.scatter(xs,ys)
plt.axis([0,101,0,25])
def covariance(x,y):
    n=len(x)
    return dot(de_mean(x),de_mean(y))/(n-1)
def de_mean(x):
    x_bar=np.mean(x)
    return [x_i-x_bar for x_i in x]
def dot(v,w):
    return sum(v_i*w_i for v_i,w_i in zip(v,w))

print('Hello world')