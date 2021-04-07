import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())

    a, b = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)

    ans = 1e6
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i]+b[j])
            elif a[i] >= b[j]:
                ans = min(ans, a[i])
            else:
                ans = min(ans, b[j])

    print(ans)

if __name__ == '__main__':
    main()