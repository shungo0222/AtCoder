from itertools import accumulate

n, w = map(int, input().split())
time = [0] * (2 * 10**5 + 1)
min_ = 2 * 10**5
max_ = 0

for _ in range(n):
    s, t, p = map(int, input().split())
    time[s] += p
    time[t] -= p
    min_ = min(min_, s)
    max_ = max(max_, t)

time = list(accumulate(time))

for i in range(min_, max_):
    if w < time[i]:
        print("No")
        exit()
        
print("Yes")