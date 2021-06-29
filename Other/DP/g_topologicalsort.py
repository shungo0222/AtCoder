# BFS式にトポロジカルソートしながらDP

from collections import deque

def main():
    n, m = map(int, input().split())
    
    g = [[] for _ in range(n)] # グラフ
    deg = [0] * n # 各頂点の入次数
    dp = [0] * n # 最長距離の保存
    
    for _ in range(m):
        x, y = map(int, input().split())
        g[x-1].append(y-1)
        deg[y-1] += 1 # 各頂点の入次数の記録
    
    queue = deque()
    
    # 入次数が０のものをキューに入れる
    for i in range(n):
        if deg[i] == 0:
            queue.append(i)
    
    # BFS
    while queue: # queueに要素がある限る繰り返す（queueが空の時のみFalse）
        x = queue.popleft()
        for i in g[x]:
            deg[i] -= 1 # エッジを消す（あるノードの入次数が１つ減る）
            if deg[i] == 0:
                queue.append(i) # 入次数が０になったらキューに入れる
                dp[i] = max(dp[i], dp[x]+1) # 最長距離の更新
    
    ans = 0
    # 全てのノードを調べる
    for i in range(n):
        ans = max(ans, dp[i])
    
    print(ans)

if __name__ == '__main__':
    main()