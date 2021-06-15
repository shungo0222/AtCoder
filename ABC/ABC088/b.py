import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    ans = 0
    j = 1
    for i in range(n):
        ans += a[i] * j
        j *= -1
    print(ans)

if __name__ == '__main__':
    main()