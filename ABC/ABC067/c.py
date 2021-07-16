import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    b = [a[0]]
    c = [a[-1]]
    for i in range(1, n):
        b.append(b[-1]+a[i])
        c.append(c[-1]+a[-(i+1)])
    c = c[::-1]
    
    ans = float('inf')
    for i in range(n-1):
        ans = min(ans, abs(b[i]-c[i+1]))
    
    print(ans)

if __name__ == '__main__':
    main()