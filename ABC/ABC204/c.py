import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())

r = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    r[a-1].append(b-1)

def dfs(i):
    if visited[i]:
        return
    visited[i] = 1
    for j in r[i]:
        dfs(j)

ans = 0

for i in range(n):
    visited = [0] * n
    dfs(i)
    ans += sum(visited)

print(ans)