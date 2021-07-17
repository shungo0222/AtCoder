from collections import  defaultdict
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    
    d = defaultdict(int)
    for i in range(k):
        d[c[i]] += 1
    
    ans = len(d.keys())
    for i in range(n-k):
        d[c[i]] -= 1
        if d[c[i]] == 0:
            del d[c[i]]
        d[c[i+k]] += 1
        
        ans = max(ans, len(d.keys()))
    
    print(ans)

if __name__ == '__main__':
    main()