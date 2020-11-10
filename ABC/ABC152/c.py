n = int(input())
p = [int(i) for i in input().split()]
min_ = p[0]
cnt = 0
for i in range(n):
    if p[i] <= min_:
        min_ = p[i]
        cnt += 1
print(cnt)