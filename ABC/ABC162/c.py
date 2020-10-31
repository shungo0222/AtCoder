import math

k = int(input())
sum_ = 0

for i in range(1, k+1):
    for j in range(1, k+1):
        x = math.gcd(i, j)
        for l in range(1, k+1):
            sum_ += math.gcd(x, l)
            
print(sum_)