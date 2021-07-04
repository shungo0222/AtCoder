# TLE

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

# dp[i][j] := 区間[i,j)番目の数列から始めて最善手を取ったときの、最終的なX-Yの値
dp = [[0]*3005 for _ in range(3005)]

# メモ化再帰
def rec(n, a, l, r):
    if l == r:
        return 0 # 範囲の個数が0の時は得点は0点
    if dp[l][r] != 0:
        return dp[l][r]
    
    tmp = 0
    if (n-(r-l))%2 == 0: # 先手
        tmp = max(a[l]+rec(n, a, l+1, r), rec(n, a, l, r-1)+a[r-1])
    else: # 後手
        tmp = min(-a[l]+rec(n, a, l+1, r), rec(n, a, l, r-1)-a[r-1])
    
    dp[l][r] = tmp # メモ化
    
    return dp[l][r]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    print(rec(n, a, 0, n))

if __name__ == '__main__':
    main()