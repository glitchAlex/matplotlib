import numpy as np
from PIL import Image
#from math import *
import matplotlib.pyplot as plt

file_path = 'C:\DEV\signals\signal03.dat'
#new_file_path = 'C:\DEV\signals\signal01new.dat'

#.dat input
data = [i.strip().split() for i in open(file_path).readlines()]
print(len(data))
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = float(data[i][j])

#outputing original .dat file
ok = [data[i][0] for i in range(len(data))]
okt = [i for i in range(len(data))]
plt.subplot(121)
plt.plot(okt,ok)

#main loop
for i in range(1,9):
    summ = 0
    for j in range(i+1):
        #print(i, j)
        summ+=ok[j]
    ok[i] = summ/(i+1)
for i in range(9, len(ok)):
    summ=0
    for j in range(i-9,i+1):
        #print(i, j)
        summ+=ok[j]
    ok[i]=summ/10

#output filtred .dat file
#ok = [data[i][0] for i in range(len(data))]
#okt = [i for i in range(len(data))]
plt.subplot(122)
plt.plot(okt,ok)
plt.axis([0,100,0, 20])
plt.show()