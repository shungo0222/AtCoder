import itertools

l, r = map(int, input().split())
if r - l >= 2018:
    print(0)
else:
    ans = 2018
    for i, j in itertools.combinations(range(l, r+1), 2):
        ans = min(ans, i * j % 2019)
    print(ans)