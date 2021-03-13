n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        slope = (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0])
        if -1 <= slope <= 1:
            ans += 1
print(ans)