n = int(input())
w = list(map(int, input().split()))
ans = float('inf')
for t in range(n-1):
    ans = min(ans, abs(sum(w[:t+1]) - sum(w[t+1:])))
print(ans)