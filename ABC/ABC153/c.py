n, k = map(int, input().split())
h = sorted([int(i) for i in input().split()])
for _ in range(k):
    h.pop()
    if h == []:
        print(0)
        exit()
print(sum(h))