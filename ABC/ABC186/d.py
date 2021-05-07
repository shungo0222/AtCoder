def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))

    cumsum = [0] * (n - 1) + [a[-1]]
    for i in range(n-2, -1, -1):
        cumsum[i] = a[i] + cumsum[i+1]
    
    ans = 0
    for i in range(0, n-1):
        ans += cumsum[i+1] - (a[i] * (n-1-i))
    print(ans)

if __name__ == '__main__':
    main()