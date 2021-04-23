import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))
print('No' if np.dot(a, b) else 'Yes')