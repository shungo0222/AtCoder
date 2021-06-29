# メモ化再帰

# これをしないと"RE（実行時エラー）"になる
import sys
sys.setrecursionlimit(10**8)

g = [] # グラフ
dp = [] # 最長のものの長さのメモ用配列

# 再帰関数
def rec(i):
    # メモされたものの再利用
    if dp[i] != -1:
        return dp[i]
    
    ans = 0
    for j in g[i]:
        ans = max(ans, rec(j)+1)
    dp[i] = ans # メモする
    
    return dp[i]

def main():
    n, m = map(int, input().split())
    
    for _ in range(n):
        g.append([])
    
    for _ in range(m):
        x, y = map(int, input().split())
        g[x-1].append(y-1)
    
    # メモされてないものを-1で初期化
    for _ in range(n):
        dp.append(-1)
    
    ans = 0
    # 全てのノードを調べる
    for i in range(n):
        ans = max(ans, rec(i))
    
    print(ans)

if __name__ == '__main__':
    main()