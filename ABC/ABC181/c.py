n = int(input())
coor = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x1 = coor[j][0] - coor[i][0]
            y1 = coor[j][1] - coor[i][1]
            x2 = coor[k][0] - coor[j][0]
            y2 = coor[k][1] - coor[j][1]
            if (coor[i][0] == coor[j][0] == coor[k][0]) \
                or (coor[i][1] == coor[j][1] == coor[k][1]):
                print('Yes')
                exit()
            elif (x1 != 0 and x2 != 0) and (y1 / x1 == y2 / x2):
                print('Yes')
                exit()

print('No')