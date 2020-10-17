x, y, a, b = map(int, input().split())

cnt = 0
i = 0

while (x * (a - 1)) < b and (x * a) < y:
    cnt += 1
    x *= a
    
if (y - x) % b == 0:
    i = 1
    
print(cnt + (y - x) // b - i)