n = int(input())
t = [[0,0,0]]
for _ in range(n):
    t.append(list(map(int,input().split())))
for i in range(n):
    time = t[i+1][0] - t[i][0]
    distance = abs(t[i+1][1] - t[i][1]) + abs(t[i+1][2] - t[i][2])
    if time < distance or (time-distance) % 2 == 1:
        print('No')
        exit()
print('Yes')