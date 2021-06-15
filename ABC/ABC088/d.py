import sys
from collections import deque
import numpy as np

class Node(object):
    def __init__(self, index, depth):
        self.index = index
        self.nears = [[index[0]+1, index[1]], [index[0]-1, index[1]], \
                    [index[0], index[1]+1], [index[0], index[1]-1]]
        self.depth = depth

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    white = np.sum(np.array(s) == '.')
    
    queue = deque()
    queue.append(Node([0, 0], 1))
    
    while queue:
        node = queue.popleft()
        nears = node.nears
        depth = node.depth
        for x, y in nears:
            if x == h-1 and y == w-1:
                print(white - depth - 1)
                exit()
            if (0 <= x < h) and (0 <= y < w) and s[x][y] == '.':
                queue.append(Node([x, y], depth+1))
                s[x][y] = '#'
    
    print(-1)

if __name__ == '__main__':
    main()