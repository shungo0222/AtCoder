x, y, z = map(int, input().split())
tmp = y / x
i = 0
while True:
    if tmp <= (i / z):
        print(i - 1)
        exit()
    i += 1