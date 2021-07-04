import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp[i][j] := 区間[i,j)のX-Yの値
    dp = [[0]*(n+2) for _ in range(n+2)]
    
    # l := 範囲の中の数字の個数
    # i := 範囲の左側
    # j := 範囲の右側+1
    for l in range(1, n+1):
        for i in range(n+1-l):
            j = i + l
            if (n-l)%2 == 0: # 先手
                dp[i][j] = max(dp[i][j-1]+a[j-1], dp[i+1][j]+a[i])
            else: # 後手
                dp[i][j] = min(dp[i][j-1]-a[j-1], dp[i+1][j]-a[i])
    
    print(dp[0][n])

if __name__ == '__main__':
    main()