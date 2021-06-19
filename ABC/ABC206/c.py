from collections import Counter, defaultdict

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    d = defaultdict(int)
    
    ans = 0
    for i in range(n-1):
        d[a[i]] += 1
        ans += (n-i-1) - c[a[i]] + d[a[i]]
    
    print(ans)

if __name__ == '__main__':
    main()