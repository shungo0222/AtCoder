from collections import Counter
from math import comb

class Cumsum(object):
    """
    cumsum
    
    Parameters
    ----------
    x : list
        the original list
    c : list
        the cumsum of x
    """
    
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
    n = int(input())
    a = list(map(int, input().split()))
    a = Cumsum(a)
    c = Counter(a.c)
    
    ans = 0
    for i in c.values():
        ans += comb(i, 2)
    
    print(ans)

if __name__ == '__main__':
    main()