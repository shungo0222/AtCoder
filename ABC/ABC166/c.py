n, m = map(int, input().split())
h = [0] + list(map(int, input().split()))
roads = [[] for _ in range(n+1)]
ans = 0
 
for _ in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)
    
for i in range(1, n+1):
    for j in roads[i]:
        if h[i] <= h[j]:
            break
    else:
        ans += 1
 
print(ans)