import matplotlib.pyplot as plt
#probably need fixes

#main
N = int(input())
points = [[0,0] for _ in range(N)]
for j in range(N):
    points[j] = [float(x) for x in input("Enter multiple value: ").split()]
#print("Number of list is: ", x) 
pointx = [0 for _ in range(len(points))]
pointy = [0 for _ in range(len(points))]
for i in range(len(points)):
    pointx[i] = points[i][0]
    pointy[i] = points[i][1]

#output
#plt.plot(pointx, pointy, '.')
import matplotlib

fig1, ax = plt.subplots()
ax.plot(pointx,pointy,'.')
ax.set_aspect(1)
plt.show()