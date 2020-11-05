n, a, b = map(int, input().split())
blue = (n // (a+b)) * a
r = n % (a+b)
if r <= a:
    print(blue+r)
else:
    print(blue+a)