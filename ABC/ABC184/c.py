a, b = map(int, input().split())
c, d = map(int, input().split())

if a == c and b == d:
    ans = 0
elif (a + b) == (c + d) \
    or (a - b) == (c - d) \
    or abs(a - c) + abs(b - d) <= 3:
    ans = 1
elif (a + b + c + d) % 2 == 0 \
    or abs(a - c) + abs(b - d) <= 6 \
    or abs((a + b) - (c + d)) <= 3 \
    or abs((a - b) - (c - d)) <= 3:
    ans = 2
else:
    ans = 3

print(ans)