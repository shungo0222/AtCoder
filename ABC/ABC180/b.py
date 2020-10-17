import math

n = int(input())
x = list(map(abs, map(int, input().split())))

print(sum(x))
print(math.sqrt(sum([i**2 for i in x])))
print(max(x))