def main():
    n, w = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    
    for i in range(n):
        for j in range(w+1):
            if j - wv[i][0] >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-wv[i][0]]+wv[i][1])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    
    print(dp[n][w])

if __name__ == '__main__':
    main()