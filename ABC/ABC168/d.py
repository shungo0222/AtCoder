import sys
from collections import deque

class Node(object):
    def __init__(self, index, nears):
        self.index = index
        self.nears = nears
        self.visit = -1
    
    def __repr__(self):
        return f'Node {{index: {self.index}, nears: {self.nears}, visit: {self.visit}}}'

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    r = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        r[a-1].append(b-1)
        r[b-1].append(a-1)
    
    nodes = []
    for i in range(n):
        nodes.append(Node(i, r[i]))
    
    queue = deque()
    queue.append(nodes[0])
    nodes[0].visit = 0
    
    while queue:
        node = queue.popleft()
        nears = node.nears
        for near in nears:
            if nodes[near].visit == -1:
                nodes[near].visit = node.index
                queue.append(nodes[near])
    
    ans = []
    for i in nodes[1:]:
        if i.visit != -1:
            ans.append(i.visit + 1)
        else:
            print('No')
            exit()
    
    print('Yes')
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()