a, b = map(int, input().split())
if a <= 5:
    print(0)
elif 6 <= a and a <= 12:
    print(b//2)
else:
    print(b)