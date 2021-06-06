def main():
    n, t = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(x[-1] + 10**9 + 1)
    
    ans = 0
    for i in range(len(x)-1):
        ans += min(t, x[i+1] - x[i])
    
    print(ans)

if __name__ == '__main__':
    main()