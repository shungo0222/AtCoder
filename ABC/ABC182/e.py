import numpy as np

h, w, n, m = map(int, input().split())
grid = np.zeros((h, w), dtype=np.int8)
for _ in range(n):
    a, b = map(int, input().split())
    grid[a - 1, b - 1] = 1
for _ in range(m):
    c, d = map(int, input().split())
    grid[c - 1, d - 1] = -1

res = np.zeros((h, w), dtype=np.int8)
for _ in range(4):
    res = res.T[::-1]
    grid = grid.T[::-1]
    tmp = np.zeros_like(res)
    H, W = tmp.shape
    for h in range(H):
        if h >= 1:
            tmp[h] |= tmp[h - 1]
        tmp[h][grid[h] == 1] = 1
        tmp[h][grid[h] == -1] = 0
    res |= tmp

print(res.sum())