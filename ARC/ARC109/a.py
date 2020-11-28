a, b, x, y = map(int, input().split())
if a <= b:
    print(x + min(2 * x, y) * (b - a))
else:
    a -= 1
    print(x + min(2 * x, y) * (a - b))