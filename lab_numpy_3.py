import numpy as np
from PIL import Image
#from math import *
import matplotlib.pyplot as plt
#import os
#import time

file_path = 'C:\DEV\ep3\lol.txt'
#new_file_path = 'C:\DEV\ep3\lol.dat'

#input
with open(file_path) as f:
    data = [[float(x)] for x in f.read().split()]
data = np.array(data)
b = np.matrix([ [0 for _ in range(data.shape[0])] for _ in range(data.shape[0])])
for i in range(b.shape[1]):
    b[i,i] = 1
    b[(i+1)%data.shape[0],i] = -1

#main loop
plt.ion()
for _ in range(255):
    plt.clf()
    plt.plot(data)
    plt.axis([0,50,0,10])
    plt.draw()
    plt.pause(0.1)
    data = data - (b.dot(data)/2)
plt.ioff()
plt.show()
print("turtle")