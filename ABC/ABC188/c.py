n = int(input())
a = list(map(int, input().split()))

x = a
y = list()
for i in range(n, 1, -1):
    for j in range(1, 2**i, 2):
        y.append(max(x[j], x[j-1]))
    x = y.copy()
    y.clear()
print(a.index(min(x)) + 1)