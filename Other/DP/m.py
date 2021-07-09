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
    
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    MOD = 10**9 + 7
    
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        c = Cumsum(dp[i-1])
        for j in range(k+1):
            dp[i][j] = c.get_sum(max(0, j-a[i-1]), j+1)%MOD
    
    print(dp[n][k])

if __name__ == '__main__':
    main()