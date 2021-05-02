n, d, h = map(int, input().split())
dh = [list(map(int, input().split())) for _ in range(n)]
dh.append([0, 0])

ans = h + 1
for i in range(n+1):
    a = (h - dh[i][1]) / (d - dh[i][0])
    b = dh[i][1] - a * dh[i][0]
    
    if b >= 0:
        flag = True
        for j in range(n+1):
            if (i != j) and (a * dh[j][0] + b < dh[j][1]):
                flag = False
                break
        if flag:
            ans = min(ans, b)

print(ans)