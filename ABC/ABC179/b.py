n = int(input())
c = []
for _ in range(n):
    d1, d2 = map(int, input().split())
    c.append(1 if d1 == d2 else 0)
    if len(c) >= 3 and min(c[-3:]) == 1:
        print('Yes')
        exit()
print('No')