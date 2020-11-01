import sys
n, k = map(int, input().split())
n %= k
x1 = n

while True:
    n = abs(x1 - k)
    x2 = abs(n - k)
    if x1 >= n and n <= x2:
        print(n) 
        sys.exit()
    else:
        x1 = n