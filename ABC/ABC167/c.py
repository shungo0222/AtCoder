n, m, x = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]
money = []

for i in range(2 ** n):
    value = [0] * (m+1)
    for j in range(n):
        if (i >> j) & 1:
            value = [value[k]+books[j][k] for k in range(m+1)]
            
    for l in range(m):
        if value[l+1] < x:
            break
        elif l == m-1:
            money.append(value[0])
            
if len(money) == 0:
    print('-1')
else:
    print(min(money))