n, d = map(int, input().split())
tree = 1
ans = 0
while True:
    ans += 1
    tree += 2 * d
    if tree >= n:
        print(ans)
        exit()
    tree += 1