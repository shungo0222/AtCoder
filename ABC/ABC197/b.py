import numpy as np

h, w, x, y = map(int, input().split())
s = [list(input()) for _ in range(h)]
s = np.array(s)
row, col = s[x-1], s[:, y-1]
ans = 0

for i in range(y, w):
    if row[i] == '.':
        ans += 1
    else: 
        break
    
for i in range(y-2, -1, -1):
    if row[i] == '.':
        ans += 1
    else: 
        break

for i in range(x, h):
    if col[i] == '.':
        ans += 1
    else: 
        break

for i in range(x-2, -1, -1):
    if col[i] == '.':
        ans += 1
    else: 
        break

print(ans+1)