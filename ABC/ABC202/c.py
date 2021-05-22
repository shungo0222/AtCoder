from collections import Counter

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    for i in range(n):
        c[i] = b[c[i] - 1]
    count = Counter(c)
    
    ans = 0
    for i in range(n):
        ans += count[a[i]]
    
    print(ans)

if __name__ == '__main__':
    main()