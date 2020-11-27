import matplotlib.pyplot as plt
#definetly need fixes. I couldn't find it on the Internet.

file_path = 'C:\DEV\lab_mpl_1\\turtle.dat'
#new_file_path = 'C:\DEV\lab_mpl_1\\turtles.dat'

#input
data = [i.strip().split() for i in open(file_path).readlines()]
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = float(data[i][j])


#main
x = [0 for _ in range(int(len(data)/2))]
y = [0 for _ in range(int(len(data)/2))]
#mx = [10000, -10000]
#my = -10000
for i in range(int(len(data)/2)):
    x[i] = data[2*i]
    y[i] = data[2*i+1]
#    if (min(x[i])<=mx[0]):
#        mx[0] = min(x[i])
#    if (max(x[i])>=mx[1]):
#        mx[1] = max(x[i])
#    if (max(y[i])>=my):
#        my = max(y[i])


#output
"""
for i in range(int(len(data)/2)):
    plt.subplot(int(len(data)/2), 2, i+1)
    plt.title('Frame ' + str(i))
    plt.plot(x[i], y[i])
    #plt.grid(which='major', color = 'k')
    #plt.grid(which='minor',color ='k', linestyle = ':')
    #plt.figure(figsize = (10,10))
    #plt.axis('square')
    i+=1
    plt.grid()
plt.show()
"""
import matplotlib

fig1, (ax,ax1,ax2,ax3,ax4,ax5) = plt.subplots(nrows=6, sharex=True)
"""
for i in range(int(len(data)/2)):
    #plt.subplot(int(len(data)/2), 2, i+1)
    plt.title('Frame ' + str(i))
    ax.plot(x[i],y[i])
    """
ax.plot(x[0],y[0])
ax.set_box_aspect(1)
plt.grid()
ax1.plot(x[1],y[1])
ax1.set_box_aspect(1)
plt.grid()
ax2.plot(x[2],y[2])
ax2.set_box_aspect(1)
plt.grid()
ax3.plot(x[3],y[3])
ax3.set_box_aspect(1)
plt.grid()
ax4.plot(x[4],y[4])
ax4.set_box_aspect(1)
plt.grid()
ax5.plot(x[5],y[5])
ax5.set_box_aspect(1)
plt.grid()
plt.show()

#test
print("turtle")