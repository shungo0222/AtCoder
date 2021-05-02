import numpy as np

n = int(input())
abcde = np.array([tuple(map(int, input().split())) for _ in range(n)])

print(min(abcde.max(axis=0)))
print(abcde.min(axis=0))