from itertools import permutations

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

ans = 0

l = [i for i in range(2, n + 1)]
for p in permutations(l):
    route = [1] + list(p) + [1]
    time = 0
    for i in range(n):
        time += t[route[i]-1][route[i+1]-1]
    if time == k:
        ans += 1
        
print(ans)