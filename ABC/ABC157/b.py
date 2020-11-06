As = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
Bs = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if Bs[i] == As[j][k]:
                As[j][k] = 0
                if (k in [0,2] and j in [0,2]) or (j == 1 and k == 1):
                    if (As[0][0] == 0 and As[1][1]  == 0 and As[2][2] == 0) \
                        or (As[0][2] == 0 and As[1][1]  == 0 and As[2][0] == 0):
                        print('Yes')
                        exit()
                if (As[j][0] == 0 and As[j][1] == 0 and As[j][2] == 0) \
                    or (As[0][k] == 0 and As[1][k] == 0 and As[2][k] == 0):
                    print('Yes')
                    exit()
print('No')