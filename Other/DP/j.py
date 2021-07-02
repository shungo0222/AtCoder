import sys

# 再帰回数上限設定
sys.setrecursionlimit(10**8)

# input処理の高速化
input = sys.stdin.readline

# -1.0で初期化、-1で初期化するとTLE
# 小数が入るとあらかじめわかっている場合は、小数で初期化した方がよりPypyの恩恵が享受できる
dp = [[[-1.0]*310 for _ in range(310)] for _ in range(310)]

# メモ化再帰
def rec(i, j, k, n):
    # メモ再利用
    if dp[i][j][k] >= 0:
        return dp[i][j][k]
    # 0での除算回避
    if i==0 and j==0 and k==0:
        return 0.0
    
    res = 0.0
    if i > 0:
        res += rec(i-1, j, k, n) * i
    if j > 0:
        res += rec(i+1, j-1, k, n) * j
    if k > 0:
        res += rec(i, j+1, k-1, n) * k
    res += n
    res *= 1.0 / (i+j+k)
    
    # メモ
    dp[i][j][k] = res
    
    return dp[i][j][k]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    one, two, three = a.count(1), a.count(2), a.count(3)
    
    print(rec(one, two, three, n))

if __name__ == '__main__':
    main()