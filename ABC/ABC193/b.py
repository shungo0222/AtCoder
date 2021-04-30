n = int(input())
apx = [list(map(int, input().split())) for _ in range(n)]
ans = 1e10
for a, p, x in apx:
    if x - a > 0:
        ans = min(ans, p)
print(-1 if ans == 1e10 else ans)