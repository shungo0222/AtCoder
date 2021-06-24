def main():
    n, w = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    v_max = 100001
    
    dp = [[float('inf') for _ in range(v_max)] for _ in range(n+1)]
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(v_max):
            if j - wv[i][1] >= 0:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-wv[i][1]]+wv[i][0])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    
    for i in range(v_max-1, -1, -1):
        if dp[n][i] <= w:
            print(i)
            exit()

if __name__ == '__main__':
    main()