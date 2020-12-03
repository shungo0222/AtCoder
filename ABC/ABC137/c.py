import math

n = int(input())
string = dict()
ans = 0
for _ in range(n):
    s = ''.join(sorted(input()))
    if s in string:
        string[s] += 1
    else:
        string[s] = 1
for i in string.values():
    if i > 1:
        ans += math.factorial(i)//(2*math.factorial(i-2))
print(ans)