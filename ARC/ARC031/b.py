import copy
from collections import deque

class Node(object):    
    def __init__(self, index):
        self.index = index
        self.nears = [[index[0]+1, index[1]], [index[0]-1, index[1]], \
                        [index[0], index[1]+1], [index[0], index[1]-1]]

def main():
    a = []
    land = 0
    for _ in range(10):
        tmp = list(input())
        land += tmp.count('o')
        a.append(tmp)
    
    for i in range(100):
        b = copy.deepcopy(a)
        x = i // 10
        y = i % 10
        
        queue = deque()
        queue.append(Node([x, y]))
        b[x][y] = 'x'
        
        cnt = 1
        while queue:
            node = queue.popleft()
            for j, k in node.nears:
                if (0 <= j < 10) and (0 <= k < 10) and b[j][k] == 'o':
                    queue.append(Node([j, k]))
                    b[j][k]= 'x'
                    cnt += 1
        
        if (a[x][y] == 'x' and cnt == land+1) or \
            (a[x][y] == 'o' and cnt == land):
            print('YES')
            exit()
    
    print('NO')

if __name__ == '__main__':
    main()