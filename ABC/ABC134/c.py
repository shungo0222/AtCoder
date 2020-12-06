n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
max_l, max_r = [a[0]], [a[-1]]
for i in range(1, n):
    max_l.append(max(max_l[i-1], a[i]))
    max_r.append(max(max_r[i-1], a[-(i+1)]))
max_r = max_r[::-1]
for i in range(n):
    if i == 0:
        print(max_r[1])
    elif i == n - 1:
        print(max_l[-2])
    else:
        print(max(max_l[i-1], max_r[i+1]))