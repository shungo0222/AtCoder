h, a = map(int, input().split())
cnt = 0
while h > 0:
    h -= a
    cnt += 1
print(cnt)