from collections import defaultdict
import math

def main():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    
    d = defaultdict(int)
    
    if m != 0:
        k = n
        for i in range(m+1):
            x = 0
            if i == 0:
                x = a[i] - 1
            elif i == m:
                x = n - a[i-1]
            else:
                x = a[i] - a[i-1] - 1
            
            if x != 0:
                k = min(k, x)
                d[x] += 1
    
    if m == 0:
        print(1)
    elif k == n:
        print(0)
    else:
        ans = 0
        for key, value in d.items():
            ans += math.ceil(key / k) * value
        print(ans)

if __name__ == '__main__':
    main()