import numpy as np

point_a = np.array([1, 2, 3, 4, 5])
point_b = np.array([5, 4, 3, 2, 1])
points = np.random.rand(4, 5)
dist=np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        point_a = points[i]
        point_b = points[j]
        d = np.sqrt(np.sum(point_a - point_b) ** 2)
        dist[i,j] = d
print(dist)