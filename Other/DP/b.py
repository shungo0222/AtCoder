def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    
    dp = [0] + [float('inf')] * (n-1)
    
    for i in range(1, n):
        for j in range(1, k+1):
            if i-j < 0:
                break
            dp[i] = min(dp[i], dp[i-j]+abs(h[i]-h[i-j]))
    
    print(dp[-1])

if __name__ == '__main__':
    main()