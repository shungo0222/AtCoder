import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dp = [[0]*401 for _ in range(400)]

class Cumsum(object):
    def __init__(self, x):
        self.x = x
        self.c = self._make_cumsum()
    
    def _make_cumsum(self):
        c = [0] * (len(self.x)+1)
    
        for i in range(len(self.x)):
            c[i+1] = c[i] + self.x[i]
        
        return c
    
    def get_sum(self, left, right):
        return (self.c[right] - self.c[left])

def rec(l, r, c):
    if dp[l][r] != 0:
        return dp[l][r]
    if l+1 == r:
        return 0
    
    tmp = float('inf')
    for i in range(l+1, r):
        tmp = min(tmp, rec(l, i, c)+rec(i, r, c))
    
    dp[l][r] = tmp + c.get_sum(l, r)
    
    return dp[l][r]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = Cumsum(a)
    
    print(rec(0, n, c))

if __name__ == '__main__':
    main()