n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]

if n == 1:
    start = 0
    stop = 10
elif n == 2:
    start = 10
    stop = 100
else:
    start = 100
    stop = 1000

for i in range(start, stop):
    num = [i for i in str(i)]
    flag = True
    for j in range(m):
        if num[sc[j][0] - 1] != str(sc[j][1]):
            flag = False
    if flag:
        print(''.join(num))
        exit()
else:
    print(-1)