import math

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    if i == 1:
        ans = math.gcd(a[i-1], a[i])
    else:
        ans = math.gcd(ans, a[i])
print(ans)