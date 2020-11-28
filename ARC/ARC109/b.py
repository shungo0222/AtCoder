import math

n = int(input())
x = 2 * (n + 1)
i = int(math.sqrt(x)) - 1
while i * (i + 1) <= x:
    i += 1
print(n - i + 2)