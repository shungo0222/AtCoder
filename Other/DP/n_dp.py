import sys

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

def main():
    input = sys.stdin.readline
    
    n = int(input())
    a = list(map(int, input().split()))
    c = Cumsum(a)
    
    dp = [[0] * (n + 1) for _ in range(n)]
    
    for w in range(2, n+1):
        for l in range(n-w+1):
            r = l + w
            
            tmp = float('inf')
            for m in range(l+1, r):
                tmp = min(tmp, dp[l][m]+dp[m][r])
            dp[l][r] = tmp + c.get_sum(l, r)
    
    print(dp[0][n])

if __name__ == '__main__':
    main()