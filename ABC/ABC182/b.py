n = int(input())
a = list(map(int, input().split()))

gcd = 0
ans = 0
for i in range(2, max(a)+1):
    tmp = 0
    for j in a:
        if j % i == 0:
            tmp += 1
    if gcd <= tmp:
        gcd = tmp
        ans = i

print(ans)