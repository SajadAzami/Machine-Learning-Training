"""PGM, 2/8/17, Sajad Azami"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

__author__ = 'sajjadaazami@gmail.com (Sajad Azami)'

d = {}

x = [1, 1, 1, 1, 0, 0, 1, 0, 1]
y = [1, 0, 1, 0, 0, 1, 0, 1, 0]

for i in range(0, len(x)):
    if (x[i], y[i]) in d.keys():
        d[(x[i], y[i])] += 1
    else:
        d[(x[i], y[i])] = 0
print(d)

d1 = {(0, 1): 12, (2, 0): 162, (0, 0): 35,
      (3, 0): 77, (1, 0): 117, (3, 1): 198,
      (4, 1): 37, (1, 1): 71, (2, 1): 186,
      (4, 0): 15}
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = []
y = []
z = []
for i in d1.items():
    x.append(i[0][0])
    y.append(i[0][1])
    z.append(i[1])
ax.bar(x, z, zs=y, zdir='y', alpha=0.8, color='r' * 4)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
