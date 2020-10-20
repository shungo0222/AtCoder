import sys
import numpy as np
input = lambda: sys.stdin.readline().rstrip()

def main():
    h, w, k = map(int, input().split())
    c = []
    ans = 0
    for _ in range(h):
        c.append(list(input()))
    grid = np.array(c)
    for i in range(2**(w+h)):
        tmp = grid.copy()
        row, col = [], []
        for j in range(w+h):
            if (i >> j) & 1:
                if j < w:
                    col.append(j)
                else:
                    row.append(j-w)
        tmp = np.delete(tmp, row, 0)
        tmp = np.delete(tmp, col, 1)
        if np.sum(tmp == '#') == k:
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    main()