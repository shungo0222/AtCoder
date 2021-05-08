import numpy as np
from math import factorial
from collections import Counter

def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)

def main():
    n = int(input())
    a = np.array(list(map(int, input().split())))
    
    c = Counter(a % 200)
    ans = 0
    for v in c.values():
        if v >= 2:
            ans += comb(v, 2)
    print(ans)

if __name__ == '__main__':
    main()