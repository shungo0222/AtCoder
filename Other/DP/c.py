def main():
    n = int(input())
    abc = [[0]*3] + [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[0, 0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[i][k] = max(dp[i][k], dp[i-1][j]+abc[i][k])
    
    print(max(dp[-1]))

if __name__ == '__main__':
    main()