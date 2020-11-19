import math

n = int(input())
min_ = n - 1
for a in range(2, int(math.sqrt(n))+1):
    if n % a == 0:
        b = n // a
        min_ = min((a-1) + (b-1), min_)
print(min_)