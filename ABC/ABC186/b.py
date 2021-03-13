import numpy as np

h, w = map(int, input().split())
l = list()
for _ in range(h):
    l.append(list(map(int, input().split())))

arr = np.array(l)

print(np.sum(arr - arr.min()))