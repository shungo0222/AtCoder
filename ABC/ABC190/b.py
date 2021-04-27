n, s, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
flag = False
for x, y in xy:
    if x < s and y > d:
        flag = True
        break
print('Yes' if flag else 'No')